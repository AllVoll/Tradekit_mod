from sqlalchemy import Column, Integer, String
from database import Base

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    binance_key = Column(String, index=True)
    binance_secret = Column(String, index=True)
    description = Column(String, index=True)