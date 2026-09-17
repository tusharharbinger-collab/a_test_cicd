from pathlib import Path
from fastapi import FastAPI, HTTPException
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
    # Deliberately left healthy — this is what ECS's own target-group health
    # check hits directly, bypassing the ALB's path prefix entirely. The
    # point of this drill is to prove the platform's *separate* live-URL
    # check (through the real ALB, with the real prefix) catches a failure
    # that a target-group health check alone would miss.
    return {"status": "ok"}


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    # Deliberately broken for this rollback drill — this is what a real
    # visitor's request through the shared ALB actually hits.
    raise HTTPException(status_code=500, detail="Deliberately broken for blue-green rollback drill")
