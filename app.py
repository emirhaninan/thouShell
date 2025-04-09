from fastapi import FastAPI
from thouShell import transform_code

app = FastAPI()

@app.post("/transform")
async def transform_endpoint(code: str):
    return {"transformed_code": transform_code(code)}
