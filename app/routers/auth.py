from fastapi import Body, Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, models,utils,oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(user_credentails:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):



    user = db.query(models.User).filter(
        models.User.email == user_credentails.username).first()


    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid creadentials")

    if not utils.verify(user_credentails.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid creadentials")

    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"token": access_token , "token_type":  "bearer"}
