import sqlalchemy as _sqlalchemy
import sqlalchemy.ext.declarative as _sqldeclarative
import sqlalchemy.orm as _sqlorm

DATABASE_URL = "sqlite:///./database.db"

engine = _sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = _sqlorm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _sqldeclarative.declarative_base()
