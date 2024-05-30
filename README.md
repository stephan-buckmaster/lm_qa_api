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

## Implemented models

For OpenAI style of API, these test models are available:

- mock-gpt-model. It generates responses saying, "Your model is mock-gpt-model;  that's just about it."
- time-of-day. It generates responses saying, "For all we know the current time is Wed May 29 21:53:46 PDT 2024," except the current time will be shown
- nonsense. It generate a response containing one of Edward Lear's Nonsense Poems. If you mention a number, you may get that many
- sonnets. It generate a response containing one of Shakespeare's sonnets. If you mention a number, you may get that many
- other. By default it will say, "Unkown model provided ....," and identify the model name

## Giants

Built on the shoulders of giants like:

- https://gist.github.com/Berkodev/77000c57ec49f41ce73b754d684f10f9#file-openai_compatible_api_example-py
- Sonnets, by Shakespeare, taken from  https://github.com/enerrio/Generate-Shakespeare-Sonnets.git
- The Book of Nonsense, by Edward Lear, from https://www.gutenberg.org/ebooks/13650.txt.utf-8 

## Usage

Usage is fairly simple. To start up the server:
```
pip install fastapi
uvicorn main:app
```

For uvicorn options, consult https://www.uvicorn.org/settings/

## Bearer Authentication:

Bt default any request will be processed.  To add
authorization, you can use our reverse proxy from
https://github.com/stephan-buckmaster/ruby-bearer-auth-proxy and put it
in front of this server.
