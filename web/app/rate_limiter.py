from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from web.app.config import REDIS_URL


def configure_limiter(app):
    Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["3 per second"],
        storage_uri=REDIS_URL,
        headers_enabled=True
    )
