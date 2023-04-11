from api.internship_database import InternshipDatabase
from api.internship_data_classes import Intern, Company, Student, Tag
from api.sql_driver import SQLDriver
from datetime import datetime
import pytest

class TestInternshipDatabase:

    @pytest.fixture
    def sql_driver(self):
        return SQLDriver(in_memory=True)
    
    @pytest.fixture
    def internship_database(self, sql_driver: SQLDriver):
        return InternshipDatabase(sql_driver)
    
    def test_get_interns(self, internship_database: InternshipDatabase, sql_driver: SQLDriver):

        interns = []
        for test in range(100):
                
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
                intern.dict()
            )

            assert internship_database.get_interns() == interns





    def test_get_companies(self, internship_database: InternshipDatabase):
        assert internship_database.get_companies() == []