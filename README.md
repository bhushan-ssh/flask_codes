# Flask Codes


Lightweight example Flask API used for learning and practicing basic routes
and simple request/response handling.

## Features
- Example REST endpoints for basic arithmetic and echoing JSON
- Demonstrates GET and POST routes and simple error handling

## Available Endpoints
- `GET /api/data` — returns a sample JSON object
- `GET /api/hello` — simple greeting JSON
- `GET /api/addition/<num1>/<num2>` — returns addition result
- `GET /api/subtract/<num1>/<num2>` — returns subtraction result
- `GET /api/multiply/<num1>/<num2>` — returns multiplication result
- `GET /api/divide/<num1>/<num2>` — returns division result (checks divide-by-zero)
- `GET /api/modulo/<num1>/<num2>` — returns modulo result (checks divide-by-zero)
- `GET /api/power/<base>/<exponent>` — returns power result
- `POST /api/echo` — echoes back posted JSON as `{ "echo": <data> }`
- `POST /api/calculate` — accepts JSON `{ "operation": "add|subtract|multiply|divide", "num1": <n>, "num2": <n> }` and returns the result
- `GET /user/<name>` — returns a JSON with username and status
- `GET /api/addition_req` — currently reads JSON via `request.get_json()` but is defined as `GET` (experimental)

## Installation
1. Create a virtual environment (recommended):

	 python -m venv venv
	 venv\Scripts\activate   # Windows

2. Install dependencies:

	 pip install Flask

3. Run the app:

	 python api.py

By default the app runs with `debug=True` on `http://127.0.0.1:5000`.

## Examples
- Get sample data:

	curl http://127.0.0.1:5000/api/data

- Addition:

	curl http://127.0.0.1:5000/api/addition/5/7

- Echo (POST):

	curl -X POST http://127.0.0.1:5000/api/echo -H "Content-Type: application/json" -d "{\"message\":\"hi\"}"

- Calculate (POST):

	curl -X POST http://127.0.0.1:5000/api/calculate -H "Content-Type: application/json" -d "{\"operation\":\"multiply\",\"num1\":4,\"num2\":5}"

## Notes
- `api.py` is intentionally simple for educational use. Improve input
	validation and error handling before using in production.
- `api.addition_req` expects JSON but is defined as `GET`; change to `POST`
	if you want to send request bodies in a standard way.

If you'd like, I can also:
- add a `requirements.txt`
- switch `addition_req` to `POST` and add tests

