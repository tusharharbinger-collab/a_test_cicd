from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="a_test_cicd", version="1.1.0")

STATIC_INDEX = Path(__file__).parent / "static" / "index.html"


@app.get("/", response_class=HTMLResponse)
def root():
    if STATIC_INDEX.exists():
        return HTMLResponse(content=STATIC_INDEX.read_text(encoding="utf-8"))
    return HTMLResponse("<h1>a_test_cicd</h1><p>Running successfully.</p>")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    return {
        "received_path": full_path,
        "message": "Hello from the Python test app",
        "version": "1.1.0",
    }
