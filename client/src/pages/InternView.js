import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "./../components/Header";

const InternView = () => {
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
  const [search, setSearch] = useState("");

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
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">
                        Edit
                    </button>
                </td>
                <td>
                    <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-full">
                        Delete
                    </button>
                </td>
              </tr>
            ))}
            <tr className="">
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">
                    Add Intern
                </button>
            </tr>
          </table>
        </div>
      </div>
    </>
  );
};

export default InternView;
