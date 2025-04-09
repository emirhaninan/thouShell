from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from thouShell import transform_code
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoint
@app.post("/transform")
async def transform_api(request: dict):
    try:
        code = request.get("code", "")
        if not code.strip():
            raise HTTPException(status_code=400, detail="No code provided")
        return {"transformed_code": transform_code(code)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Frontend route
@app.get("/")
async def read_index():
    return FileResponse("index.html")
