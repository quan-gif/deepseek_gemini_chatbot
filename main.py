from fastapi import FastAPI
import uvicorn
from app.routers.chat import router
app = FastAPI(title = "CHATBOT",version = "1.0.0")
app.include_router(router)
@app.get("/health")
def checK_health():
    return{"status":"ok"}
    return "This is minh quan's chatbot"
if __name__ == "__main__":uvicorn.run("main:app",host = "0.0.0.0",port = 8000,reload = True)




