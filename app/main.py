

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.thouformers import (
    FunctionTransformer,
    ClassTransformer,
    ControlFlowTransformer,
    CommentTransformer
)

app = FastAPI(title="ThouShell API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ShakespeareanTransformer:
    def __init__(self):
        self.transformers = [
            FunctionTransformer(),
            ClassTransformer(),
            ControlFlowTransformer(),
            CommentTransformer()
        ]
    
    def transform(self, code: str) -> str:
        for transformer in self.transformers:
            code = transformer.transform_code(code)
        return code

transformer = ShakespeareanTransformer()

@app.post("/transform")
async def transform_code(request: dict):
    try:
        code = request.get("code", "")
        if not code.strip():
            raise ValueError("No code provided")
        
        transformed = transformer.transform(code)
        return {"transformed_code": transformed}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("app/static/index.html")