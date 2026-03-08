

from fastapi import FastAPI
from routes import router  

app = FastAPI(title="Python TOTP Microservice")
app.include_router(router)