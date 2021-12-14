import aioredis

from app.core.config import settings


async def set(key: str, value: str) -> None:
    redis = aioredis.from_url(settings.REDIS_URL)
    async with redis.client() as conn:
        conn.set(key, value)


async def get(key: str) -> str:
    redis = aioredis.from_url(settings.REDIS_URL)
    async with redis.client() as conn:
        val = conn.get(key)
    return val
