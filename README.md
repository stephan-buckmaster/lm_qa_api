# Mock Language Model API Services

## Introduction

Building web applications that integrate with APIs, like [OpenAI's](https://platform.openai.com/docs/api-reference/introduction), can be both exciting and challenging.

## Purpose

This project provides a mock API service that mimics the interface
of popular APIs like OpenAI's. It is designed to help developers test
their integrations seamlessly without worrying about API rate limits,
registration processes, or incurring costs.

## Key Features

- **Stable Interface**: Offers a consistent and reliable interface for testing.
- **No Registration Required**: Begin testing immediately without the need for API keys or authentication processes.
- **Mock Responses**: Receive mock responses that simulate real API calls, helping you debug and validate your integration logic.

## Giants
Built on the shoulders of giants like:


- https://gist.github.com/Berkodev/77000c57ec49f41ce73b754d684f10f9#file-openai_compatible_api_example-py
- Sonnets, by Shakespeare, taken from  https://github.com/enerrio/Generate-Shakespeare-Sonnets.git
- The Book of Nonsense, by Edward Lear, from https://www.gutenberg.org/ebooks/13650.txt.utf-8 

Usage:

```
pip install fastapi
uvicorn main:app
```


## Bearer Authentication:

To add authorization, you can use our reverse proxy from https://github.com/stephan-buckmaster/ruby-bearer-auth-proxy and put it in front of this server.
