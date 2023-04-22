from pydantic import BaseModel
from typing import Optional


class StudentView(BaseModel):  # Dataclass
    name: str
    grade_point_average: float
    student_email: str
    internship_name: str
    begin_date: str
    end_date: Optional[str]
    company_name: str
    company_email: str


class Intern(BaseModel):  # Dataclass
    id: int
    name: str
    begin_date: str
    end_date: Optional[str]
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
