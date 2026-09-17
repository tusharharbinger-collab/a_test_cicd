# a_test_cicd

Minimal Python backend using FastAPI.

## Intended Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

> **Note**: Enter this command manually in the onboarding wizard, since a bare Python repository has no `scripts.start` equivalent for the platform to auto-detect.

## Routes

- `GET /`: Interactive web dashboard, real-time health probe monitor, and API path tester
- `GET /healthz`: Health check returning `{"status": "ok"}`
- `GET /{full_path:path}`: Catch-all route echoing received path:
  ```json
  {
    "received_path": "{full_path}",
    "message": "Hello from the Python test app",
    "version": "1.0.0"
  }
  ```
