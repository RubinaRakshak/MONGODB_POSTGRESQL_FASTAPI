from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas import CreateJobRequest
from .database import get_db
from .models import Job


app = FastAPI()

@app.post("/")
def create(details: CreateJobRequest, db: Session = Depends(get_db)):
    to_create = Job(
        title=details.title,
        description=details.description
    )
    db.add(to_create)
    db.commit()
    return { 
        "success": True,
        "created_id": to_create.id
    }

@app.get("/")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == id).first()

@app.post('/signup/')
def signup(name: str,email:str,password:str,phone:str):
    if '@' not in email:
        return {"Email ID Invalid"}
    if len(password)<5 or "#" not in password:
        return {"Password is not secure please input 6 digit password and add # for more security"}
    user_exist = py_functions.check_user_exist(email,cnxn)
    if user_exist==0:
        signup_query = py_functions.signup_data(name,email,password,phone)
        cursor.execute(signup_query)
        return {"status":"Signed Up Please login with same creds."}
    else:
        return {"status":'Email ID already exist.'}


@app.post('/login/')
def login(email: str,password:str):
    user_exist = py_functions.check_user_details(email,password,cnxn)
    if user_exist>0:
        return {"Status":"Login Successful Access Granted"}
    else:
        return {"Status":"Login error Access not Granted"}
