from fastapi import FastAPI
import app.routes.api as api

app = FastAPI()

app.include_router(api.router)
