import posthog

from app.core.config import settings


class PosthogClient:
    """ Singleton class for posthog client """

    _instance = None

    def _initialize(self) -> posthog:
        posthog.host = settings.POSTHOG_HOST
        posthog.api_key = settings.POSTHOG_API_KEY
        return posthog

    def get_client(self) -> posthog:
        return posthog

    def __new__(cls) -> "PosthogClient":
        if cls._instance is None:
            if not settings.POSTHOG_HOST or not settings.POSTHOG_API_KEY:
                raise Exception("Cannot initialize Posthog. Config not set.")
            cls._instance = super(PosthogClient, cls).__new__(cls)
            cls._instance._initialize()

        return cls._instance

