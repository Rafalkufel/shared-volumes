import os
from fastapi import FastAPI
from app.tasks import exemplary_task

app = FastAPI()


@app.get("/")
async def root():
    exemplary_task.apply_async()
    path_to_save = "/MyDir"
    created_files = os.listdir(path_to_save)
    return {"message": created_files}
