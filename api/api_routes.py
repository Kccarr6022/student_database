from create_api import create_api
from internship_database import InternshipDatabase
from internship_data_classes import Intern, Company, Student, Tag, StudentView
import uvicorn

app = create_api()
internship_database = InternshipDatabase()

@app.get("/student_interns")
def get_student_interns():
    return internship_database.get_student_interns()

@app.get("/interns")
def get_interns():
    return internship_database.get_interns()


@app.get("/companies")
def get_companies():
    return internship_database.get_companies()


@app.get("/students")
def get_students():
    return internship_database.get_students()


@app.get("/tags")
def get_tags():
    return internship_database.get_tags()

@app.post("/student_intern")
def post_student_intern(student_intern: StudentView):
    return internship_database.add_student_intern(student_intern)


@app.post("/intern")
def add_intern(intern: Intern):
    return internship_database.add_intern(intern)


@app.post("/company")
def add_company(company: Company):
    return internship_database.add_company(company)


@app.post("/student")
def add_student(student: Student):
    return internship_database.add_student(student)


@app.post("/tag")
def add_tag(tag: Tag):
    return internship_database.add_tag(tag)

@app.put("/student_intern")
def update_student_intern(student_intern: StudentView):
    return internship_database.update_student_view(student_intern)

@app.put("/intern")
def update_intern(intern: Intern):
    return internship_database.update_intern(intern)


@app.put("/company")
def update_company(company: Company):
    return internship_database.update_company(company)


@app.put("/student")
def update_student(student: Student):
    return internship_database.update_student(student)


@app.put("/tag")
def update_tag(tag: Tag):
    return internship_database.update_tag(tag)

@app.delete("/student_intern")
def delete_student_intern(student_intern: StudentView):
    return internship_database.delete_student_view(student_intern)


@app.delete("/intern")
def delete_intern(intern: Intern):
    return internship_database.delete_intern(intern)


@app.delete("/company")
def delete_company(company: Company):
    return internship_database.delete_company(company)


@app.delete("/student")
def delete_student(student: Student):
    return internship_database.delete_student(student)


@app.delete("/tag")
def delete_tag(tag: Tag):
    return internship_database.delete_tag(tag)


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
