# 🐍 Pippy Debugger Backend

A FastAPI server backend that powers the debugging functionality for the Pippy project. This backend analyzes Python code and returns helpful debugging suggestions using an LLM.

## Features

- **FastAPI** backend  
- **LLM-powered debugging** for Python programs  
- `/debug` endpoint with real-time suggestions  
- **Context mode**: explains code in a kid-friendly way  

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/yourusername/pippy-debugger-backend.git
cd pippy-debugger-backend
```
### Set up Environment
Rename `.example.env` → `.env` and add your `GOOGLE_API_KEY`
```env
GOOGLE_API_KEY = your_api_key_here
```
### Install the dependencies
```bash
pip install -r requirements.txt
```
### Run the Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Usage

### Endpoint:  
**POST** 
```
/debug?code={your_python_code}&context={true|false}
```
### Params:
- `code`: Python code snippet (string)  
- `context`: `true | false` → enable kid-friendly explanations  
### Example Request:  
```sh
curl -X POST "http://localhost:8000/debug?code=How%20do%20I%20create%20a%20Python%20class&context=False"
```
### Response Format:
```json
{
  "answer": "Debugging suggestions for your python code....",
}
```

## Testing
After running the server, open in your browser
```
http://localhost:8000/
```
You'll see a hello message from Pippy-Debugger

## License

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE)

## Credits

This project was developed as part of **DMP 2025** by [Harshit Verma](https://github.com/therealharshit).
