/* Select from internship table */
SELECT * FROM internship;

/* Select from internship table under condition */

SELECT * FROM internship WHERE id = 1;
SELECT * FROM internship WHERE name = 'Software Engineering Intern';

/* Select from view table */
SELECT * FROM student_view;

/* Select from tag table */
SELECT * FROM tag;

/* Select from tag table under condition */

SELECT * FROM tag WHERE id = 1; /* Select from tag table under id condition*/
SELECT * FROM tag WHERE name = 'Java'; /* Select from tag table under name condition*/

/* Select from company table */
SELECT * FROM company;

/* Select from company table under condition */

SELECT * FROM company WHERE id = 1; /* Select from company table under id condition*/
SELECT * FROM company WHERE name = 'Google'; /* Select from company table under name condition*/

/* Select from student table */
SELECT * FROM student;

/* Select from student table under condition */

SELECT * FROM student WHERE id = 1; /* Select from student table under id condition*/
SELECT * FROM student WHERE name = 'John';

BEGIN TRANSACTION; /* We intend to create a view dataclass and insert an entire view all at once with a transaction */

/* Insert into company table */
INSERT INTO company (name, company_email) VALUES ('Google', 'google@gmail.com');

/* Insert into student table */
INSERT INTO student (name, grade_point_average, student_email) VALUES ('John', 3.5, 'johnc421421@eagle.fgcu.edu');

INSERT INTO internship (name, begin_date, end_date, student_id, company_id)
VALUES ('Software Engineering Intern', '2018-01-01', '2018-05-31', 1, 1);

/* Insert into tag table */
INSERT INTO tag (name)
VALUES ('Java');

END TRANSACTION;

/* update internship table */
UPDATE internship SET name = 'Software Engineering Intern' WHERE id = 1;

/* update tag table */
UPDATE tag SET name = 'Java' WHERE id = 1;

/* update company table */
UPDATE company SET name = 'Google', company_email = 'google@gmail.com' WHERE id = 1;

/* update student table */
UPDATE student SET name = 'John', grade_point_average = 3.5 WHERE id = 1;


/* delete from internship table */
DELETE FROM internship WHERE name = 'Software Engineering Intern';

/* delete from tag table */
DELETE FROM tag WHERE name = 'Java';

/* delete from company table */
DELETE FROM company WHERE company_email = 'google@gmail.com';

/* delete from student table */
DELETE FROM student WHERE name = 'John';


/*

Here is Parameterized Statements in Python with SQLite3

We use these functions to insert data into the database:


def get_students_view(self) -> List[StudentView]:
        """Gets all students.

        Returns:
            List[StudentView]: The List of students.
        """
        sql = "SELECT * FROM student_view"
        self.driver.execute_raw(sql)
        tuples = self.driver.cursor.fetchall()
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
            Tag(**{field: tuple[i] for i, field in enumerate(Tag.__fields__.keys())})
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
            INSERT INTO internship (id, name, begin_date, end_date, student_id, company_id)
            VALUES (:id, :name, :begin_date, :end_date, :student_id, :company_id)
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
            INSERT INTO companies (name, company_email)
            VALUES (:name, :company_email)
            """,
            company.dict(),
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
*/