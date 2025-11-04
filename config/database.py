from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔗 URL database dari Railway (punya kamu)
DATABASE_URL = "postgresql://postgres:eEVgAaMBSqAqnIAkcHuLUAKuxSRKHiNN@mainline.proxy.rlwy.net:57119/railway"

# Engine koneksi
engine = create_engine(DATABASE_URL, echo=False)

# Session untuk query
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base untuk model ORM
Base = declarative_base()

# Dependency untuk session (gaya uanku_api)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
