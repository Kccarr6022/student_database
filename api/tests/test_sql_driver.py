from api.sql_driver import SQLDriver
import pytest
class TestSQLDriver:
    
    @pytest.fixture
    def sql_driver(self):
        return SQLDriver(in_memory=True)

    def test_execute_raw(self, sql_driver: SQLDriver):
        for i in range(100):
            sql_driver.execute_raw(f"CREATE TABLE test{i} (id INTEGER PRIMARY KEY, name TEXT)")
            sql_driver.execute_raw(f"INSERT INTO test{i} (name) VALUES ('test{i}')")

            assert sql_driver.cursor.execute(f"SELECT * FROM test{i}").fetchone() == (1, f"test{i}")
    
    def test_execute_statement(self, sql_driver: SQLDriver):
        for i in range(100):
            sql_driver.execute_raw(f"CREATE TABLE test{i} (id INTEGER PRIMARY KEY, name TEXT)")
            sql_driver.execute_statement(f"INSERT INTO test{i} (name) VALUES (:name)", {"name": f"test{i}"})

            assert sql_driver.cursor.execute(f"SELECT * FROM test{i}").fetchone() == (1, f"test{i}")