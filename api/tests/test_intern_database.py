from api.internship_database import InternshipDatabase
from api.internship_data_classes import StudentView, Intern, Company, Student, Tag
from api.sql_driver import SQLDriver
from datetime import datetime
from typing import List
import pytest


class TestInternshipDatabase:
    @pytest.fixture
    def sql_driver(self):
        return SQLDriver(in_memory=True)

    @pytest.fixture
    def internship_database(self, sql_driver: SQLDriver):
        return InternshipDatabase(sql_driver)

    def test_get_students_view(
        self, internship_database: InternshipDatabase, sql_driver: SQLDriver
    ):
        students = []
        for test in range(1, 10):
            student_view = StudentView(
                name=f"test{test}",
                grade_point_average=test,
                student_email=f"{test}@fgcu.edu",
                internship_name=f"test{test}",
                begin_date=str(datetime(year=2000, month=test, day=test)),
                end_date=None,
                company_name=f"test{test}",
                company_email=f"{test}@company.com",
            )

            sql_driver.execute_raw("SELECT * FROM student")
            new_student_id = sql_driver.cursor.lastrowid
            sql_driver.execute_raw("SELECT * FROM company")
            new_company_id = sql_driver.cursor.lastrowid

            sql_driver.execute_transaction(
                sql=[
                    "INSERT INTO student(name, grade_point_average, student_email) VALUES (:name, :grade_point_average, :student_email)",
                    "INSERT INTO company(name, company_email) VALUES (:name, :company_email);",
                    "INSERT INTO internship(name, begin_date, end_date, student_id, company_id) VALUES (:name, :begin_date, :end_date, :student_id, :company_id);",
                ],
                params=[
                    {
                        "name": student_view.name,
                        "grade_point_average": student_view.grade_point_average,
                        "student_email": student_view.student_email,
                    },
                    {
                        "name": student_view.company_name,
                        "company_email": student_view.company_email,
                    },
                    {
                        "name": student_view.internship_name,
                        "begin_date": student_view.begin_date,
                        "end_date": student_view.end_date,
                        "student_id": new_student_id,
                        "company_id": new_company_id,
                    },
                ]
            )

            students.append(student_view)

            assert internship_database.get_students_view() == students

    def test_get_interns(
        self, internship_database: InternshipDatabase, sql_driver: SQLDriver
    ):
        interns = []
        for test in range(10):
            assert internship_database.get_interns() == interns

            intern = Intern(
                id=test,
                name=f"test{test}",
                begin_date=str(datetime.now()),
                end_date=str(datetime.now()),
                company_id=test,
                student_id=test,
            )

            interns.append(intern)

            sql_driver.execute_statement(
                "INSERT INTO internship (id, name, begin_date, end_date, company_id, student_id) VALUES (:id, :name, :begin_date, :end_date, :company_id, :student_id)",
                intern.dict(),
            )

            assert internship_database.get_interns() == interns

    def test_get_companies(
        self, internship_database: InternshipDatabase, sql_driver: SQLDriver
    ):
        companies: List[Company] = []

        for test in range(10):
            assert internship_database.get_companies() == companies

            company = Company(
                id=test, name=f"test{test}", company_email=f"{test}@gmail.com"
            )

            companies.append(company)

            sql_driver.execute_statement(
                "INSERT INTO company (id, name, company_email) VALUES (:id, :name, :company_email)",
                company.dict(),
            )

            assert internship_database.get_companies() == companies

    def test_get_students(
        self, internship_database: InternshipDatabase, sql_driver: SQLDriver
    ):
        students: List[Student] = []

        for test in range(10):
            assert internship_database.get_students() == students

            student = Student(
                id=test,
                name=f"test{test}",
                grade_point_average=test,
                student_email=f"{test}@gmail.com",
            )

            students.append(student)

            sql_driver.execute_statement(
                "INSERT INTO student (id, name, grade_point_average, student_email) VALUES (:id, :name, :grade_point_average, :student_email)",
                student.dict(),
            )

            assert internship_database.get_students() == students

    def test_get_tags(
        self, internship_database: InternshipDatabase, sql_driver: SQLDriver
    ):
        tags: List[Tag] = []

        for test in range(10):
            assert internship_database.get_tags() == tags

            tag = Tag(
                id=test,
                name=f"test{test}",
            )

            tags.append(tag)

            sql_driver.execute_statement(
                "INSERT INTO tag (id, name) VALUES (:id, :name)",
                tag.dict(),
            )

            assert internship_database.get_tags() == tags

    def test_add_intern(self, internship_database: InternshipDatabase):
        interns = []
        for test in range(1, 10):
            intern = Intern(
                id=test,
                name=f"test{test}",
                begin_date=str(datetime.now()),
                end_date=str(datetime.now()),
                company_id=test,
                student_id=test,
            )
            internship_database.add_intern(intern)
            interns.append(intern)

            assert internship_database.get_interns() == interns

    def test_add_company(self, internship_database: InternshipDatabase):
        companies = []
        for test in range(1, 10):
            company = Company(id=test, name="test", company_email=f"{test}@")

            internship_database.add_company(company)
            companies.append(company)

            assert internship_database.get_companies() == companies
