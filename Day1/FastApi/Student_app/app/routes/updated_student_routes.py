from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional
from app.models.student import Student
from app.database.db import students_db
from app.dependencies.student_dependency import get_student_by_id

router = APIRouter()

#Request body to create a new student
@router.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED )
def create_student(student: Student):
    students_db.append(student)
    #return {"message": "Student created successfully", "student": student}
    return student

#Read all students - (GET)
@router.get("/students", response_model=List[Student], status_code=status.HTTP_200_OK)
def get_students():
    return students_db

#Read One (using Dependency Injection)
@router.get("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def get_student(student: Student = Depends(get_student_by_id)):
    return student

#update (using Dependency Injection)
@router.put("/students/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student(updated_student: Student, 
                   student: Student = Depends(get_student_by_id)):
    for index, s in enumerate(students_db):
        if s.id == student.id:
            students_db[index] = updated_student
            return updated_student
        
#delete (using Dependency Injection)
@router.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student: Student = Depends(get_student_by_id)):
    for index, s in enumerate(students_db):
        if s.id == student.id:
            del students_db[index]
            return

#Query parameter to filter students by course
@router.get("/courses")
def filter_studentcourse(course: Optional[str] = None):
    if course:
        filtered_students = [student for student in students_db if course in student.courses]
        return filtered_students
    return students_db