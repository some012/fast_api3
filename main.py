from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from tables import driver, trip, fio
from app import models
from app.db import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(driver.router)
app.include_router(trip.router)
app.include_router(fio.router)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>Test-test-test root</h1>"