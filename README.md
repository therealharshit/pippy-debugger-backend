# 🐍 Pippy Debugger Server

A FastAPI server backend that powers the debugging functionality for the Pippy project. This server analyzes Python code and returns helpful debugging suggestions using an LLM.

## Features

- FastAPI-based RESTful server
- Integrates with LLMs to analyze Python code
- `/debug` endpoint for real-time code analysis and tips
- `/context` endpoint for code contextualization

## To Run the Server

### Install the dependencies
```sh
pip install -r requirements.txt
```
### Run the Server
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```
