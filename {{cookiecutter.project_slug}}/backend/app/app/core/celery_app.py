import sentry_sdk

from celery import Celery
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from app.core.config import settings

if settings.SENTRY_DSN:
    sentry_sdk.init(
        settings.SENTRY_DSN,
        environment=settings.SERVER_ENV,
        integrations=[CeleryIntegration(), RedisIntegration()],
    )


celery_app = Celery("worker")
celery_app.conf.broker_url = settings.REDIS_URL
celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
