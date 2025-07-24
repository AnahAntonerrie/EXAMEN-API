from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello",status_code=200)
def read_hello():
    return "Hello world"

@app.get("/welcome",status_code=200 )
def welcome_user(name: str):
    return {"message":f"welcome {name}"}


class student(BaseModel):
    Reference:str
    FirstName:str
    LastName:str
    Age:int

@app.get("/students", status_code=200)
def get_students():
    return students_db

@app.put("/students", status_code=200)
def update_or_add_student(student: Student):
    global students_db
    for idx, existing_student in enumerate(students_db):
        if existing_student.Reference == student.Reference:
            if existing_student != student:
                students_db[idx] = student
            return {"message": "Student updated or already exists", "students": students_db}
    students_db.append(student)
    return {"message": "Student added", "students": students_db}
