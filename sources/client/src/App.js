import React from "react";
import MainContent from "./components/MainContent";
import SidePromt from "./components/SidePromt";


function App() {
  return (
    <div style={{display:"flex"}}>
      <SidePromt/>
      <MainContent />
    </div>
  );
}

export default App;