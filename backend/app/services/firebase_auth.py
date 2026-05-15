import firebase_admin
from firebase_admin import auth, credentials
from app.core.config import settings
from app.core.logging import logger

firebase_app = None


def init_firebase():
    global firebase_app
    if firebase_app:
        return firebase_app

    if settings.firebase_credentials_path:
        cred = credentials.Certificate(settings.firebase_credentials_path)
        firebase_app = firebase_admin.initialize_app(cred, {
            "projectId": settings.firebase_project_id,
        })
    else:
        firebase_app = firebase_admin.initialize_app()

    return firebase_app


def verify_firebase_token(id_token: str):
    try:
        init_firebase()
        decoded = auth.verify_id_token(id_token)
        logger.info("Verified Firebase user %s", decoded.get("uid"))
        return {
            "uid": decoded.get("uid"),
            "email": decoded.get("email"),
            "name": decoded.get("name"),
            "admin": decoded.get("admin", False),
            "claims": decoded,
        }
    except Exception as exc:
        logger.warning("Firebase token verify failed: %s", exc)
        return None
