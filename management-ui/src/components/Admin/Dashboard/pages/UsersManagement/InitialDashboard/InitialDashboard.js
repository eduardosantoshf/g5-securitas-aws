import React from "react";
import "./InitialDashboard.css";
import img from "./img3.png";

function InitialDashboard() {
  return (
    <div className="initialDashboard">
        <h1 className="titleDashboard">Welcome to G5 Securitas !</h1>
        <p className="contentDashboard">SecCom is a company that ensures critical buildings are not broken into, through the installation and operation of CCTV cameras on-premises.</p>
        <p className="contentDashboard">The goal of G5 Securitas is to help SecCom with their transition to the digital world, creating an automatic system that can identify intruders without human-intervention and act accordingly.</p>
        <div className="img">
          <img src={img} alt="logo" />
        </div>
        
    </div>

  );
}

export default InitialDashboard;
