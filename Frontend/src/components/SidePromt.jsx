import React from "react";
import "./SidePromt.css";

function SidePromt() {
  return (
    <div className="container side">
      <div className="content">
        <h2>About</h2>
        <p>
        This chatbot interacts with an object-oriented programming (OOP) agent designed to answer questions about concepts such as objects, classes, inheritance, and encapsulation in programming. This agent uses OOP to manage and organize source code, helping to create programs that are modular, easy to maintain and extend, combining structured data and data processing methods.
        </p>
        <h2>Example Question</h2>
        <ol>
          <li>What is object-oriented programming (OOP)?</li>
          <li>What is the concept of "object" in OOP and how is it used?</li>
          <li> What is the difference between class and object in OOP? </li>
          <li>
          How does inheritance in OOP help in reusing source code?{" "}
          </li>
          <li>What is encapsulation and why is it important in OOP? </li>
          <li>
          How is OOP different from procedural programming?
          </li>
        </ol>
      </div>
    </div>
  );
}

export default SidePromt;
