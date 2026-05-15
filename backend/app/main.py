from fastapi import FastAPI

app = FastAPI(title="AI Memory Platform", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "AI Memory Platform Running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
