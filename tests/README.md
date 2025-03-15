# Tests Directory

This directory contains automated tests for the FastAPI application. The tests ensure that the API endpoints work correctly and handle various scenarios appropriately.

## Structure

```
tests/
├── __init__.py          <-- Makes the tests directory a Python package
├── README.md            <-- This file
└── test_api.py          <-- Tests for API endpoints
```

## Test Coverage

The `test_api.py` file includes tests for:

1. **Health Check Endpoint** (`/health`)
   - Verifies the endpoint returns 200 OK
   - Checks correct response format

2. **Root Endpoint** (`/`)
   - Verifies the endpoint returns 200 OK
   - Validates API status message

3. **Prediction Endpoint** (`/predict`)
   - Tests valid input data (Iris flower measurements)
   - Validates response structure and data types
   - Tests error handling for:
     - Missing features
     - Invalid data types

## Running the Tests

From the project root directory, run:

```bash
docker-compose exec api pytest tests/
```

Expected output:
```
============================= test session starts ==============================
platform linux -- Python 3.10.x, pytest-8.x.x, pluggy-1.x.x
rootdir: /app
plugins: anyio-4.x.x
collected 5 items

tests/test_api.py .....                                               [100%]

============================== 5 passed in 1.37s ==============================
```

## Adding New Tests

When adding new tests:
1. Follow the existing pattern in `test_api.py`
2. Use the `TestClient` from FastAPI for API calls
3. Add clear assertions with meaningful error messages
4. Group related tests together
5. Add comments explaining test scenarios 