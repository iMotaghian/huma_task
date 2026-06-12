from sqlalchemy import Column, Integer, String, Boolean,DateTime,func
from database import Base


class Logs(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String, index=True)
    message = Column(String(300))
    timestamp = Column(DateTime,default=func.now())
     