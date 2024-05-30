import asyncio
import json
import time
from time_of_day_handler import TimeOfDayHandler
from echo_model_handler import EchoModelHandler
from shakespeare_sonnet_handler import ShakespeareSonnetHandler
from default_handler import DefaultHandler
from shakespeare_sonnet_handler import ShakespeareSonnetHandler
import uuid

from typing import Optional, List

from pydantic import BaseModel, Field

from starlette.responses import StreamingResponse
from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="OpenAI-compatible API")

COMPLETION_HANDLERS = {
        'mock-gpt-model': EchoModelHandler,
        'time-of-day': TimeOfDayHandler,
        'sonnets': ShakespeareSonnetHandler,
}

# data models
class Message(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: Optional[str]
    messages: List[Message]
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.1
    stream: Optional[bool] = False

    def complete(self):
        handler = COMPLETION_HANDLERS.get(self.model, DefaultHandler)
        return handler(self).complete()

async def _resp_async_generator(text_resp: str, request: ChatCompletionRequest):
    # let's pretend every word is a token and return it over time
    tokens = text_resp.split(" ")

    for i, token in enumerate(tokens):
        chunk = {
            "id":  str(uuid.uuid4()),
            "object": "chat.completion.chunk",
            "created": time.time(),
            "model": request.model,
            "choices": [{"delta": {"content": token + " "}}],
        }
        yield f"data: {json.dumps(chunk)}\n\n"
        await asyncio.sleep(0.01)
    yield "data: [DONE]\n\n"


@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    resp_content = request.complete()
    if request.stream:
        return StreamingResponse(
            _resp_async_generator(resp_content, request), media_type="application/x-ndjson"
        )

    return {
        "id": str(uuid.uuid4()),
        "object": "chat.completion",
        "created": time.time(),
        "model": request.model,
        "choices": [{"message": Message(role="assistant", content=resp_content)}],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
