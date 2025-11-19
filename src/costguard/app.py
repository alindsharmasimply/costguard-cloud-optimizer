from fastapi import FastAPI

app = FastAPI(title="costguard", version="0.0.1")

@app.get('/health')
def health_check():
    return {"status": "ok"}