from time import sleep
from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, bcrypt, jwt
from models import *
from routes import register_routes
from utils.init_roles import init_roles


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Routes "métier"
    register_routes(app)

    # Endpoints de test/monitoring
    @app.route("/", methods=["GET"])
    def root():
        return "Hello world", 200

    @app.route("/health", methods=["GET"])
    def health():
        return "OK", 200

    # --- Init DB au démarrage (Flask 3.x : pas de before_first_request) ---
    # Petit retry pour attendre Postgres malgré 'service_healthy'
    with app.app_context():
        for attempt in range(10):
            try:
                db.create_all()
                init_roles()
                app.logger.info("Database initialized.")
                break
            except Exception as e:
                app.logger.warning(f"DB init attempt {attempt+1}/10 failed: {e}")
                sleep(2)
        else:
            app.logger.exception("DB init failed after retries.")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0", port=5000)
