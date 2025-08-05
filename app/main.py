import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="VaultNote",
    description="A Secure, Taggable Personal Notes App",
    version="0.1.0",
)

# Basic CORS setup for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "VaultNote API is running!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Important: use string format for reload to work
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
