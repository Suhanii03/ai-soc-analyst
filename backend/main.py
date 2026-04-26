from fastapi import FastAPI
from backend.api.routes import router
app = FastAPI(title="AI SOC Analyst")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI SOC Analyst Running"}