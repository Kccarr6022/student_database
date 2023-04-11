CREATE TABLE IF NOT EXISTS student (
    id integer PRIMARY KEY,
    name varchar(50) NOT NULL,
    grade_point_average double NOT NULL,
    student_email varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS company (
    id integer PRIMARY KEY,
    name varchar(50) NOT NULL,
    company_email varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS internship (
    id integer PRIMARY KEY,
    name varchar(50) NOT NULL,
    begin_date datetime NOT NULL,
    end_date datetime NOT NULL,
    student_id integer NOT NULL,
    company_id integer NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (company_id) REFERENCES company(id)
);

CREATE TABLE IF NOT EXISTS tag (
    id integer PRIMARY KEY,
    name varchar(50) NOT NULL
);