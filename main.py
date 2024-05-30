import asyncio
import json
import time

from typing import Optional, List

from pydantic import BaseModel, Field

from starlette.responses import StreamingResponse
from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="OpenAI-compatible API")

class BaseHandler:
    def __init__(self, request):
        self.request = request

    def model(self):
        return self.request.model

class SimpleMockHandler(BaseHandler):
    def complete(self):
            return "We are only echoing your model as " + self.model() + ";  and that's just about it"


class TimeOfDayHandler(BaseHandler):
    def complete(self):
            return "For all we know the current time is " + time.strftime('%a %b %d %H:%M:%S %Z %Y')

class DefaultHandler(BaseHandler):
    def complete(self):
            return "Unkown model " + self.model

COMPLETION_HANDLERS = {
        'mock-gpt-model': SimpleMockHandler,
        'time-of-day': TimeOfDayHandler,
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

    def wascomplete(self):
        if self.model == 'mock-gpt-model':
            return "We are only echoing your model as " + self.model + ";  and that's just about it"
        elif self.model == 'time-of-day':
            return "For all we know the current time is " + time.strftime('%a %b %d %H:%M:%S %Z %Y')
        else:
            return "Unkown model"

async def _resp_async_generator(text_resp: str, request: ChatCompletionRequest):
    # let's pretend every word is a token and return it over time
    tokens = text_resp.split(" ")

    for i, token in enumerate(tokens):
        chunk = {
            "id": i,
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
        "id": "1337",
        "object": "chat.completion",
        "created": time.time(),
        "model": request.model,
        "choices": [{"message": Message(role="assistant", content=resp_content)}],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
