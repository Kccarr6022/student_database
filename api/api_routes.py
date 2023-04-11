from create_api import create_api
from internship_database import InternshipDatabase
from internship_data_classes import Intern, Company, Student, Tag
import uvicorn

app = create_api()
internship_database = InternshipDatabase()


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

@app.post("/intern")
def add_intern(intern: Intern):
    return internship_database.add_intern(intern)

@app.post("/company")
def add_company(company: Company):
    return internship_database.add_company(company)

@app.post("/student")
def add_student(student: Student):
    return internship_database.add_student(student)

@app.post('/tag')
def add_tag(tag: Tag):
    return internship_database.add_tag(tag)

@app.put('/intern')
def update_intern(intern: Intern):
    return internship_database.update_intern(intern)

@app.put('/company')
def update_company(company: Company):
    return internship_database.update_company(company)

@app.put('/student')
def update_student(student: Student):
    return internship_database.update_student(student)

@app.put('/tag')
def update_tag(tag: Tag):
    return internship_database.update_tag(tag)

@app.delete('/intern')
def delete_intern(intern: Intern):
    return internship_database.delete_intern(intern)

@app.delete('/company')
def delete_company(company: Company):
    return internship_database.delete_company(company)

@app.delete('/student')
def delete_student(student: Student):
    return internship_database.delete_student(student)

@app.delete('/tag')
def delete_tag(tag: Tag):
    return internship_database.delete_tag(tag)

if __name__ == "__main__":
    uvicorn.run(app, port=5000)