from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base
from app.utils.hashing import get_password_hash, verify_password


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nulable=False, unique=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, username, email, password, *args, **kwargs):
        self.username = username
        self.email = email
        self.password = get_password_hash(password)

    def check_password(self, password):
        return verify_password(password, self.password)
