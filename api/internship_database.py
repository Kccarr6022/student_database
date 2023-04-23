from typing import Optional, List
from internship_data_classes import StudentView, Intern, Company, Student, Tag
from sql_driver import SQLDriver


class InternshipDatabase:
    def __init__(self, driver: Optional[SQLDriver] = None):
        self.driver = driver or SQLDriver()
        self.define_database()

    def define_database(self):
        """Executes the raw ddl statements to define the database structure."""

        # Students View
        self.driver.execute_raw(
            """
            CREATE VIEW IF NOT EXISTS student_view AS
            SELECT student.id, student.name, student.grade_point_average, student.student_email, internship.name AS internship_name, internship.begin_date, internship.end_date, company.name AS company_name, company.company_email
            FROM student
            LEFT JOIN internship ON student.id = internship.student_id
            LEFT JOIN company ON internship.company_id = company.id;
            """
        )

        # Students table
        self.driver.execute_raw(
            """
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                grade_point_average FLOAT NOT NULL,
                student_email VARCHAR(50) NOT NULL
            );
            """
        )

        # Companies table
        self.driver.execute_raw(
            """
            CREATE TABLE IF NOT EXISTS company (
                id integer PRIMARY KEY AUTOINCREMENT,
                name varchar(50) NOT NULL,
                company_email varchar(50) NOT NULL
            );
            """
        )

        # Internships table
        self.driver.execute_raw(
            """
            CREATE TABLE IF NOT EXISTS internship (
                id integer PRIMARY KEY AUTOINCREMENT,
                name varchar(50) NOT NULL,
                begin_date date NOT NULL,
                end_date date,
                student_id integer NOT NULL,
                company_id integer NOT NULL,
                FOREIGN KEY (student_id) REFERENCES student(id),
                FOREIGN KEY (company_id) REFERENCES company(id)
            );
            """
        )

        # Tags table
        self.driver.execute_raw(
            """
            CREATE TABLE IF NOT EXISTS tag (
                id integer PRIMARY KEY AUTOINCREMENT,
                name varchar(50) NOT NULL
            );
            """
        )

    def get_student_interns(self) -> List[StudentView]:
        """Gets all students.

        Returns:
            List[StudentView]: The List of students.
        """
        sql = "SELECT * FROM student_view"
        self.driver.execute_raw(sql)
        tuples = self.driver.cursor.fetchall(
        )
        print(tuples)
        # Remove the id field from the tuples
        tuples = [tuple[1:] for tuple in tuples]
        return [
            StudentView(
                **{
                    field: tuple[i]
                    for i, field in enumerate(StudentView.__fields__.keys())
                }
            )
            for tuple in tuples
        ]

    def get_students(self) -> List[Student]:
        """Gets all projects.

        Returns:
            List[Project]: The List of projects.
        """
        sql = "SELECT * FROM student"
        self.driver.execute_raw(sql)
        tuples = self.driver.cursor.fetchall()
        return [
            Student(
                **{field: tuple[i] for i, field in enumerate(Student.__fields__.keys())}
            )
            for tuple in tuples
        ]

    def get_interns(self) -> List[Intern]:
        """Gets all interns.

        Returns:
            List[Intern]: The List of interns.
        """
        sql = "SELECT * FROM internship"
        self.driver.execute_raw(sql)
        tuples = self.driver.cursor.fetchall()
        return [
            Intern(
                **{field: tuple[i] for i, field in enumerate(Intern.__fields__.keys())}
            )
            for tuple in tuples
        ]

    def get_companies(self) -> List[Company]:
        """Gets all companies.

        Returns:
            List[Company]: The List of companies.
        """
        sql = "SELECT * FROM company"
        self.driver.execute_raw(sql)
        tuples = self.driver.cursor.fetchall()
        return [
            Company(
                **{field: tuple[i] for i, field in enumerate(Company.__fields__.keys())}
            )
            for tuple in tuples
        ]

    def get_tags(self) -> List[Tag]:
        """Gets all tags.

        Returns:
            List[Tag]: The List of tags.
        """
        sql = "SELECT * FROM tag"
        self.driver.execute_raw(sql)
        tuples = self.driver.cursor.fetchall()
        return [
            Tag(**{field: tuple[i]
                for i, field in enumerate(Tag.__fields__.keys())})
            for tuple in tuples
        ]

    def get_intern_by_student_id(self, student_id: int) -> Intern:
        """Gets an intern by student id.

        Args:
            student_id (int): The student id.

        Returns:
            Intern: The intern.
        """
        sql = "SELECT * FROM interns WHERE student_id = ?"
        self.driver.execute_statement(sql, params={"student_id": student_id})
        tuple = self.driver.cursor.fetchone()
        return Intern(
            **{field: tuple[i] for i, field in enumerate(Intern.__fields__.keys())}
        )

    def get_company_by_id(self, id: int) -> Company:
        """Gets a company by id.

        Args:
            id (int): The id.

        Returns:
            Company: The company.
        """
        sql = "SELECT * FROM companies WHERE id = ?"
        self.driver.execute_statement(sql, params={"id": id})
        tuple = self.driver.cursor.fetchone()
        return Company(
            **{field: tuple[i] for i, field in enumerate(Company.__fields__.keys())}
        )

    def get_student_by_id(self, id: int) -> Student:
        """Gets a student by id.

        Args:
            id (int): The id.

        Returns:
            Student: The student.
        """
        sql = "SELECT * FROM students WHERE id = ?"
        self.driver.execute_statement(sql, params={"id": id})
        tuple = self.driver.cursor.fetchone()
        return Student(
            **{field: tuple[i] for i, field in enumerate(Student.__fields__.keys())}
        )

    def get_tag_by_id(self, id: int) -> Tag:
        """Gets a tag by id.

        Args:
            id (int): The id.

        Returns:
            Tag: The tag.
        """
        sql = "SELECT * FROM tags WHERE id = ?"
        self.driver.execute_statement(sql, params={"id": id})
        tuple = self.driver.cursor.fetchone()
        return Tag(**{field: tuple[i] for i, field in enumerate(Tag.__fields__.keys())})

    def get_intern_by_id(self, id: int) -> Intern:
        """Gets an intern by id.

        Args:
            id (int): The id.

        Returns:
            Intern: The intern.
        """
        sql = "SELECT * FROM interns WHERE id = ?"
        self.driver.execute_statement(sql, params={"id": id})
        tuple = self.driver.cursor.fetchone()
        return Intern(
            **{field: tuple[i] for i, field in enumerate(Intern.__fields__.keys())}
        )
    
    def add_student_intern(self, student_view: StudentView):
        """Adds a student view.

        Args:
            student_view (StudentView): The student view to add.
        """
        self.driver.execute_raw("SELECT * FROM student")
        new_student_id = self.driver.cursor.lastrowid + 1
        self.driver.execute_raw("SELECT * FROM company")
        new_company_id = self.driver.cursor.lastrowid + 1

        self.driver.execute_transaction(
            sql=[
                "INSERT INTO student(id, name, grade_point_average, student_email) VALUES (:id, :name, :grade_point_average, :student_email)",
                "INSERT INTO company(id, name, company_email) VALUES (:id, :name, :company_email);",
                "INSERT INTO internship(name, begin_date, end_date, student_id, company_id) VALUES (:name, :begin_date, :end_date, :student_id, :company_id);",
            ],
            params=[
                {
                    "id": new_student_id,
                    "name": student_view.name,
                    "grade_point_average": student_view.grade_point_average,
                    "student_email": student_view.student_email,
                },
                {
                    "id": new_company_id,
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

    def add_student(self, student: Student):
        """Adds a student.

        Args:
            student (Student): The student to add.
        """
        self.driver.execute_statement(
            """
            INSERT INTO students (name, grade_point_average, student_email)
            VALUES (:name, :grade_point_average, :student_email)
            """,
            student.dict(),
        )

    def add_intern(self, intern: Intern):
        """Adds an intern.

        Args:
            intern (Intern): The intern to add.
        """
        self.driver.execute_statement(
            """
            INSERT INTO internship (name, begin_date, end_date, student_id, company_id)
            VALUES (:name, :begin_date, :end_date, :student_id, :company_id)
            """,
            intern.dict(),
        )

    def add_tag(self, tag: Tag):
        """Adds a tag.

        Args:
            tag (Tag): The tag to add.
        """
        self.driver.execute_statement(
            """
            INSERT INTO tags (name)
            VALUES (:name)
            """,
            tag.dict(),
        )

    def add_company(self, company: Company):
        """Adds a company.

        Args:
            company (Company): The company to add.
        """
        self.driver.execute_statement(
            """
            INSERT INTO company (name, company_email)
            VALUES (:name, :company_email)
            """,
            company.dict(),
        )

    def update_student_intern(self, student_view: StudentView):
        """Updates a student view.

        Args:
            student_view (StudentView): The student view to update.
        """
        self.driver.execute_transaction(
            sql=[
                "UPDATE students SET name = :name, grade_point_average = :grade_point_average, student_email = :student_email WHERE id = :id",
                "UPDATE company SET name = :name, company_email = :company_email WHERE id = :id",
                "UPDATE internship SET name = :name, begin_date = :begin_date, end_date = :end_date WHERE id = :id",
            ],
            params=[
                {
                    "id": student_view.student_id,
                    "name": student_view.name,
                    "grade_point_average": student_view.grade_point_average,
                    "student_email": student_view.student_email,
                },
                {
                    "id": student_view.company_id,
                    "name": student_view.company_name,
                    "company_email": student_view.company_email,
                },
                {
                    "id": student_view.internship_id,
                    "name": student_view.internship_name,
                    "begin_date": student_view.begin_date,
                    "end_date": student_view.end_date,
                },
            ],
        )

    def update_intern(self, intern: Intern):
        """Updates an intern.

        Args:
            intern (Intern): The intern to update.
        """
        self.driver.execute_statement(
            """
            UPDATE interns
            SET name = :name,
                begin_date = :begin_date,
                end_date = :end_date
            WHERE id = :id
            """,
            intern.dict(),
        )

    def update_student(self, student: Student):
        """Updates a student.

        Args:
            student (Student): The student to update.
        """
        self.driver.execute_statement(
            """
            UPDATE students
            SET name = :name,
                grade_point_average = :grade_point_average,
                student_email = :student_email
            WHERE id = :id
            """,
            student.dict(),
        )

    def update_company(self, company: Company):
        """Updates a company.

        Args:
            company (Company): The company to update.
        """
        self.driver.execute_statement(
            """
            UPDATE companies
            SET name = :name,
                company_email = :company_email
            WHERE id = :id
            """,
            company.dict(),
        )

    def update_tag(self, tag: Tag):
        """Updates a tag.

        Args:
            tag (Tag): The tag to update.
        """
        self.driver.execute_statement(
            """
            UPDATE tags
            SET name = :name
            WHERE id = :id
            """,
            tag.dict(),
        )

    def delete_student(self, student: Student):
        """Deletes a student.

        Args:
            student (Student): The student to delete.
        """
        self.driver.execute_statement(
            """
            DELETE FROM students
            WHERE id = :id
            """,
            student.dict(),
        )

    def delete_intern(self, intern: Intern):
        """Deletes an intern.

        Args:
            intern (Intern): The intern to delete.
        """
        self.driver.execute_statement(
            """
            DELETE FROM interns
            WHERE id = :id
            """,
            intern.dict(),
        )

    def delete_company(self, company: Company):
        """Deletes a company.

        Args:
            company (Company): The company to delete.
        """
        self.driver.execute_statement(
            """
            DELETE FROM companies
            WHERE id = :id
            """,
            company.dict(),
        )

    def delete_tag(self, tag: Tag):
        """Deletes a tag.

        Args:
            tag (Tag): The tag to delete.
        """
        self.driver.execute_statement(
            """
            DELETE FROM tags
            WHERE id = :id
            """,
            tag.dict(),
        )
