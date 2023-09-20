from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger
from celery.app.log import TaskFormatter

redis_url = f"redis://:test-pass@redis:6379/0"


@after_setup_logger.connect
@after_setup_task_logger.connect
def setup_task_logger(logger, *_, **__):
    for handler in logger.handlers:
        handler.setFormatter(TaskFormatter("%(message)s"))


celery_worker = Celery(__name__)
celery_worker.conf.broker_url = redis_url
celery_worker.conf.result_backend = redis_url
celery_worker.conf.task_default_queue = "test-queue"
celery_worker.conf.broker_connection_retry_on_startup = True
celery_worker.conf.timezone = "UTC"

celery_worker.conf.imports = ["app.tasks"]