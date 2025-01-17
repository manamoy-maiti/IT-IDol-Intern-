from fastapi import FastAPI , Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# this is Pydantic model
class Student(BaseModel):
    name: str
    age: int
    cgpa: float

# this is student data 
student = {
    1: {
        "name": "manamoy",
        "age": 21,
        "cgpa": 7.6 
    },
    2: {
        "name": "rakesh",
        "age": 22,
        "cgpa": 8.2 
    },
    3: {
        "name": "anshu",
        "age": 24,
        "cgpa": 8.5 
    }
}



@app.get("/")
def read_item():
    return {"message": "hey"}


@app.get("/student_details/{student_id}", response_model=Student)
def get_student(student_id: int = Path(..., description="Enter the student id for details")):
    student_data = student.get(student_id)
    if student_data:
        return Student(**student_data) #Convert the dictionary to a Student model  #multiple args are passing 
    return {"errors": "student not found"}
    

@app.get("/student_name/")
def get_student(name : Optional[str]): 
    for student_id in student:
        if student[student_id]['name'] == name :
            return student[student_id]

    return {"data":"not found"}    

@app.post("student_form/ {student_id}")
def student_form(student_id : int , student: Student):
    if student_id in student:
        return {"error": "student is already present"}

    students = students[student_id]    
    return student[student_id]