from fastapi import FastAPI, Depends, HTTPException,status,Request
from sqlalchemy.orm import Session
from datetime import datetime
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Huma Qualification Task")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/log/", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
def create_log(request: Request, log : schemas.LogCreateSchema, db : Session = Depends(get_db)):
    db_log = models.Logs(client_id = log.client_id, message = log.message)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {"status":"ok","log_id":db_log.id}

@app.get("/log/{client_id}")
def get_logs(client_id: str, db: Session = Depends(get_db)):
    return db.query(models.Logs).filter(models.Logs.client_id == client_id).order_by(models.Logs.timestamp.desc()).limit(20).all()

    

