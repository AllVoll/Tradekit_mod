from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.db.session import get_db
from app.models.api_key import ApiKey as ApiKeyModel
from app.schemas.api_key import ApiKeyCreate, ApiKeyUpdate, ApiKeyOut

router = APIRouter()

class ApiKey(Base):
    pass

@router.get("/{api_key_id}", response_model=ApiKeyOut)
def read_api_key(api_key_id: int, db: Session = Depends(get_db)):
    api_key = db.query(ApiKey).filter(ApiKey.id == api_key_id).first()
    if not api_key:
        raise HTTPException(status_code=404, detail="API key not found")
    return api_key

@router.post("/", response_model=ApiKeyOut)
def create_api_key(api_key: ApiKeyCreate, db: Session = Depends(get_db)):
    db_api_key = ApiKeyModel(**api_key.dict())
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

@router.put("/{api_key_id}", response_model=ApiKeyOut)
def update_api_key(api_key_id: int, api_key: ApiKeyUpdate, db: Session = Depends(get_db)):
    db_api_key = db.query(ApiKey).filter(ApiKey.id == api_key_id).first()
    if not db_api_key:
        raise HTTPException(status_code=404, detail="API key not found")
    for field, value in api_key:
        setattr(db_api_key, field, value)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

@router.delete("/{api_key_id}")
def delete_api_key(api_key_id: int, db: Session = Depends(get_db)):
    db_api_key = db.query(ApiKey).filter(Api_Key.id == api_key_id).first()
if not db_api_key:
raise HTTPException(status_code=404, detail="API key not found")
db.delete(db_api_key)
db.commit()
return {"detail": "API key deleted"}