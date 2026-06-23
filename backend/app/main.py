from fastapi import FastAPI

app = FastAPI(
    title="AI Career Intelligence Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Career Intelligence Platform 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }