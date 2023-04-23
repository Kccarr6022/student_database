from pydantic import BaseModel, validator
from typing import Optional
from datetime import date, datetime


class StudentView(BaseModel):  # Dataclass
    name: str 
    grade_point_average: float
    student_email: str
    internship_name: str
    begin_date: date
    end_date: Optional[date]
    company_name: str
    company_email: str

class Intern(BaseModel):  # Dataclass
    id: int
    name: str
    begin_date: date
    end_date: Optional[date]
    company_id: int
    student_id: int


class Company(BaseModel):  # Dataclass
    id: int
    name: str
    company_email: str


class Student(BaseModel):  # Dataclass
    id: int
    name: str
    grade_point_average: float
    student_email: str


class Tag(BaseModel):  # Dataclass
    id: int
    name: str
