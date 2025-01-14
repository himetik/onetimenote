import os
from flask import Flask
from web.app.routes import note_bp
from web.app.error_handlers import ErrorHandler
from web.app.rate_limiter import configure_limiter


def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback_secret_key")
    app.register_blueprint(note_bp)
    ErrorHandler(app)
    configure_limiter(app)
    return app


app = create_app()


if __name__ == "__main__":
    app().run()
