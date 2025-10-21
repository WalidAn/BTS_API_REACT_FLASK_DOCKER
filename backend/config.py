# backend/config.py
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://user:userpassword@localhost:5432/flaskdb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Meilleure robustesse des connexions
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,       # revalide les connexions
        "pool_recycle": 1800,        # recycle périodiquement
    }
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt_dev")
