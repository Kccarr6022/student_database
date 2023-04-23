import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "./../components/Header";

const InternView = () => {
  const [search, setSearch] = useState("");
  const [addIntenForm, setAddInternForm] = useState(false);
  const [addInten, setAddIntern] = useState({
    name: "",
    gradePointAverage: "",
    studentEmail: "",
    internshipName: "",
    beginDate: "",
    endDate: "",
    companyName: "",
    companyEmail: "",
  });
  const [editInternForm, setEditInternForm] = useState(false);
  const [internInEdit, setInternInEdit] = useState({
    name: "",
    gradePointAverage: "",
    studentEmail: "",
    internshipName: "",
    beginDate: "",
    endDate: "",
    companyName: "",
    companyEmail: "",
  });
  const [studentsView, setStudentsView] = useState([
    {
      name: "Kaden Carr",
      gradePointAverage: "3.5",
      studentEmail: "kccarr6022@eagle.fgcu.edu",
      internshipName: "Software Intern",
      beginDate: "1/20/2021",
      endDate: "",
      companyName: "GTT",
      companyEmail: "wad",
    },
  ]);

  const handleEnter = (e) => {
    if (e.key === "Enter") {
      axios
        .get(`http://localhost:5000/students_view?search=${search}`)
        .then((response) => {
          setStudentsView(response.data);
        });
    }
  };

  const handleSearch = (e) => {
    setSearch(e.target.value);
  };

  const getInterns = async () => {
    axios.get("http://localhost:5000/students_view").then((response) => {
      setStudentsView(response.data);
    });
  };

  const addIntern = async () => {
    setStudentsView([...studentsView, addInten]);
    axios
      .post("http://localhost:5000/students_view", { addInten })
      .then((response) => {
        setStudentsView(response.data);
      });
      setAddInternForm(false);
  };

  const editIntern = async (intern) => {
    setEditInternForm(true);
    setInternInEdit(intern)
  };

  const updateIntern = async () => {
    axios
      .put("http://localhost:5000/students_view", { internInEdit })
      .then((response) => {
        setStudentsView(response.data);
      });
  };

  const deleteIntern = async (id) => {
    setStudentsView(studentsView.filter((student) => student.id !== id));
    axios
      .delete(`http://localhost:5000/students_view/${id}`)
      .then((response) => {
        setStudentsView(response.data);
      });
  };


  useEffect(() => {
    getInterns();
  }, []);

  return (
    <>
      <Header />
      <div className="w-screen">
        <div className="w-fit mx-auto block my-12 gap-4">
          <label className="text-4xl mx-auto font-semibold">
            Search:
            <input
              type="text"
              className="ml-4 pl-5 border-solid border-blue-black border- rounded-full drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]"
              onKeyDown={(event) => handleEnter(event)}
            />
          </label>
          <label className="text-4xl mx-auto font-semibold ml-4">
            Filter by:
            <select className="ml-4 pl-5 border-solid border-blue-black border- rounded-full drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)]">
              <option value="name">Name</option>
              <option value="company">Company</option>
              <option value="location">Location</option>
              <option value="position">Position</option>
              <option value="start">Start Date</option>
              <option value="end">End Date</option>
            </select>
          </label>
        </div>
        <div className="flex flex-col gap-4 my-24">
          <table className="font-medium text-xl mx-auto w-10/12 text-center">
            <tr className="font-bold">
              <td>Name</td>
              <td>GPA</td>
              <td>Email</td>
              <td>Internship Name</td>
              <td>Start Date</td>
              <td>End Date</td>
              <td>Company</td>
              <td>Position</td>
              <td></td>
              <td></td>
            </tr>

            {studentsView.map((student) => (
              <tr>
                <td>{student.name}</td>
                <td>{student.gradePointAverage}</td>
                <td>{student.studentEmail}</td>
                <td>{student.internshipName}</td>
                <td>{student.beginDate}</td>
                <td>{student.endDate}</td>
                <td>{student.companyName}</td>
                <td>{student.companyEmail}</td>
                <td>
                  <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
                  onClick={() => editIntern(student)}
                  >
                    Edit
                  </button>
                </td>
                <td>
                  <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-full"
                  onClick={
                    () => deleteIntern(student.id)
                  }>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
            <tr className="">
              <button
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full"
                onClick={() => setAddInternForm(!addIntenForm)}
              >
                Add Intern
              </button>
            </tr>
          </table>
        </div>
      </div>
      {addIntenForm && (
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-1/2 h-1/2 bg-white z-50 shadow-lg rounded-xl">
          <button className="absolute top-0 left-0 px-4 py-2 text-2xl bg-red-600" onClick={() => setAddInternForm(!addIntenForm)}>X</button>
          <h1 className="text-4xl font-semibold text-center">
            Add Intern
          </h1>
          <form onSubmit={
            (e) => {
              e.preventDefault();
              addIntern();
            }
          }>
            <div className="grid lg:grid-cols-2 gap-4 mt-10 mx-5">
            <div className="flex flex-row items-center my-2">
              <input
                type="text"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                placeholder="Name"
                onChange={(e) => setAddIntern({ ...addInten, name: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="GPA"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setAddIntern({ ...addInten, gpa: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Email"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setAddIntern({ ...addInten, email: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Company"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setAddIntern({ ...addInten, internshipName: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Position"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setAddIntern({ ...addInten, startDate: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Start Date"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setAddIntern({ ...addInten, endDate: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="End Date"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setAddIntern({ ...addInten, companyName: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Supervisor"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setAddIntern({ ...addInten, companyEmail: e.target.value })}
              />
            </div>
            </div>
            <div className="flex justify-center">
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full w-48 mx-autolex flex-col gap-4 my-12">
              Submit
            </button>
            </div>
          </form>
        </div>
      )}
      {editInternForm && 
      (
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-1/2 h-1/2 bg-white z-50 shadow-lg rounded-xl">
          <button className="absolute top-0 left-0 px-4 py-2 text-2xl bg-red-600" onClick={() => setEditInternForm(!editInternForm)}>X</button>
          <h1 className="text-4xl font-semibold text-center">
            Edit Intern Data
          </h1>
          <form onSubmit={
            (e) => {
              e.preventDefault();
              updateIntern();
            }
          }>
            <div className="grid lg:grid-cols-2 gap-4 mt-10 mx-5">
            <div className="flex flex-row items-center my-2">
              <input
                type="text"
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                placeholder="Name"
                value={internInEdit.name}
                onChange={(e) => setInternInEdit({ ...internInEdit, name: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="GPA"
                value={internInEdit.gradePointAverage}
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setInternInEdit({ ...internInEdit, gpa: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Student Email"
                value={internInEdit.studentEmail}
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setInternInEdit({ ...internInEdit, email: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Company"
                value={internInEdit.internshipName}
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setInternInEdit({ ...internInEdit, internshipName: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Start Date"
                value={internInEdit.startDate}
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setInternInEdit({ ...internInEdit, startDate: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="End Date"
                value={internInEdit.endDate}
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setInternInEdit({ ...internInEdit, endDate: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="End Date"
                value={internInEdit.companyName}
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setInternInEdit({ ...internInEdit, companyName: e.target.value })}
              />
            </div>
            <div className="flex flex-row items-center my-2"> 
              <input
                type="text"
                placeholder="Company Email"
                value={internInEdit.companyEmail}
                className="ml-4 pl-5 border-solid border-blue-black border- rounded-2xl drop-shadow-[0_1.2px_1.2px_rgba(0,0,0,0.8)] h-12 w-full"
                onChange={(e) => setInternInEdit({ ...internInEdit, companyEmail: e.target.value })}
              />
            </div>
            </div>
            <div className="flex justify-center">
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full w-48 mx-autolex flex-col gap-4 my-12">
              Submit
            </button>
            </div>
          </form>
        </div>
      )}
    </>
  );
};

export default InternView;
