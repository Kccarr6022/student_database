from api.sql_driver import SQLDriver
import pytest
import sqlite3


class TestSQLDriver:
    @pytest.fixture
    def sql_driver(self):
        return SQLDriver(in_memory=True)

    def test_execute_raw(self, sql_driver: SQLDriver):
        for i in range(10):
            sql_driver.execute_raw(
                f"CREATE TABLE test{i} (id INTEGER PRIMARY KEY, name TEXT)"
            )
            sql_driver.execute_raw(f"INSERT INTO test{i} (name) VALUES ('test{i}')")

            assert sql_driver.cursor.execute(f"SELECT * FROM test{i}").fetchone() == (
                1,
                f"test{i}",
            )

    def test_execute_statement(self, sql_driver: SQLDriver):
        for i in range(10):
            sql_driver.execute_raw(
                f"CREATE TABLE test{i} (id INTEGER PRIMARY KEY, name TEXT)"
            )
            sql_driver.execute_statement(
                f"INSERT INTO test{i} (name) VALUES (:name)", {"name": f"test{i}"}
            )

            assert sql_driver.cursor.execute(f"SELECT * FROM test{i}").fetchone() == (
                1,
                f"test{i}",
            )

    def test_execute_transaction(self, sql_driver: SQLDriver):
        # First we create multiple tables

        sql_driver.execute_raw(
            "CREATE TABLE table1 (id INTEGER PRIMARY KEY, name TEXT);"
        )
        sql_driver.execute_raw(
            "CREATE TABLE table2 (id INTEGER PRIMARY KEY, name TEXT);"
        )
        sql_driver.execute_raw(
            "CREATE TABLE table3 (id INTEGER PRIMARY KEY, name TEXT);"
        )

        table1 = []
        table2 = []
        table3 = []

        for transaction in range(1, 10):
            sql_driver.execute_transaction(
                sql=[
                    "INSERT INTO table1 (name) VALUES (:name)",
                    "INSERT INTO table2 (name) VALUES (:name)",
                    "INSERT INTO table3 (name) VALUES (:name)",
                ],
                params=[
                    {"name": f"test{transaction} table1"},
                    {"name": f"test{transaction} table2"},
                    {"name": f"test{transaction} table3"},
                ]
            )

            table1.append((transaction, f"test{transaction} table1"))
            table2.append((transaction, f"test{transaction} table2"))
            table3.append((transaction, f"test{transaction} table3"))

            assert sql_driver.cursor.execute("SELECT * FROM table1").fetchall() == table1
            assert sql_driver.cursor.execute("SELECT * FROM table2").fetchall() == table2
            assert sql_driver.cursor.execute("SELECT * FROM table3").fetchall() == table3
            