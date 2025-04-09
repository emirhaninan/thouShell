from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from thouShell import transform_code  # Make sure filename matches exactly!

app = FastAPI()

# Enable CORS (allows your frontend to communicate with the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transform")
async def transform_route(request: dict):
    try:
        code = request.get("code", "")
        if not code:
            raise HTTPException(status_code=400, detail="No code provided")
        return {"transformed_code": transform_code(code)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")  # This handles the root URL
async def home():
    return {"message": "ThouShell API is running! POST to /transform to use it."}
