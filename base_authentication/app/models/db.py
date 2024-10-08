from .database import SessionLocal, engine


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
