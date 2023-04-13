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

    def test_get_student_view(self, internship_database: InternshipDatabase, sql_driver: SQLDriver):
        for test in range(10):

            student_view = StudentView(
                id=test,
                name=f"test{test}",
                grade_point_average=test,
                student_email=f"{test}@fgcu.edu",
                internship_name=f"test{test}",
                begin_date=str(datetime(year=2000, month=test, day=test)),
                end_date=None,
                company_name=f"test{test}",
                company_email=f"{test}@company.com",
            )

            student = Student(
                id=student_view.id,
                name=student_view.name,
                grade_point_average=student_view.grade_point_average,
                student_email=student_view.student_email,
            )

            company = Company(
                id=test,
                name=student_view.company_name,
                company_email=student_view.company_email,
            )

            intern = Intern(
                id=test,
                name=student_view.internship_name,
                begin_date=str(datetime.now()),
                end_date=None,
                company_id=test,
                student_id=test,
            )

            sql_driver.execute_statements(
                """INSERT INTO student (id, name, grade_point_average, student_email) VALUES (:id, :name, :grade_point_average, :student_email)
                INSERT INTO company (id, name, company_email) VALUES (:id, :name, :company_email)
                INSERT INTO internship (id, name, begin_date, end_date, company_id, student_id) VALUES (:id, :name, :begin_date, :end_date, :company_id, :student_id)""",
                [student.dict(), company.dict(), intern.dict()],
            )

            assert internship_database.get_student_view(student.id) == [
                {
                    "id": intern.id,
                    "name": intern.name,
                    "begin_date": intern.begin_date,
                    "end_date": intern.end_date,
                    "company_id": intern.company_id,
                    "student_id": intern.student_id,


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

    def test_get_companies(self, internship_database: InternshipDatabase, sql_driver: SQLDriver):
        
        companies: List[Company] = []

        for test in range(10):
                
                assert internship_database.get_companies() == companies
    
                company = Company(
                    id=test,
                    name=f"test{test}",
                    company_email=f"{test}@gmail.com"
                )
    
                companies.append(company)
    
                sql_driver.execute_statement(
                    "INSERT INTO company (id, name, company_email) VALUES (:id, :name, :company_email)",
                    company.dict(),
                )
    
                assert internship_database.get_companies() == companies

    def test_get_students(self, internship_database: InternshipDatabase, sql_driver: SQLDriver):
        
        students: List[Student] = []

        for test in range(10):
                
                assert internship_database.get_students() == students
    
                student = Student(
                    id=test,
                    name=f"test{test}",
                    grade_point_average=test,
                    student_email=f"{test}@gmail.com"
                )

                students.append(student)

                sql_driver.execute_statement(
                    "INSERT INTO student (id, name, grade_point_average, student_email) VALUES (:id, :name, :grade_point_average, :student_email)",
                    student.dict(),
                )

                assert internship_database.get_students() == students

    
    def test_get_tags(self, internship_database: InternshipDatabase, sql_driver: SQLDriver):
        
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
        for test in range(10):
                
            intern = Intern(
                id=test,
                name=f"test{test}",
                begin_date=str(datetime.now()),
                end_date=str(datetime.now()),
                company_id=test,
                student_id=test,
            )
            internship_database.add_intern(intern)

            assert internship_database.get_interns() == [intern]

    def test_add_company(self, internship_database: InternshipDatabase):
        for test in range(10):
            company = Company(
                id=test,
                name="test",
                company_email=f"{test}@"
            )

            internship_database.add_company(company)

            assert [Company(**record.dict() for record in sql_driver.cursor.execute("SELECT * FROM company"))][0] == company

