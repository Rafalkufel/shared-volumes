from uuid import uuid4
import logging
from app.celery import celery_worker
import pathlib
import os

logger = logging.getLogger(__name__)

@celery_worker.task
def exemplary_task():
    path_to_save = "/MyDir"
    if not os.path.exists(path_to_save):
        os.mkdir(path_to_save)

    file_name = f"CreatedInCelery{uuid4()}"

    file_path = os.path.join(path_to_save, file_name)
    pathlib.Path(file_path).touch()
    logger.debug(f"created file name: {file_name}")
    logger.debug(os.listdir(path_to_save))
