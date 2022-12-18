import React, { Component } from "react";
import "./Dashboard.css";
import Sidebar from "./nestedComponents/Sidebar";
import Topbar from "./nestedComponents/Topbar";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Cameras from "./pages/UsersManagement/Cameras/Cameras";
import Alarms from "./pages/UsersManagement/Alarms/Alarms";
import InitialDashboard from "./pages/UsersManagement/InitialDashboard/InitialDashboard";
import Intrusions from "./pages/UsersManagement/Intrusions/Intrusions";

function Dashboard() {
  return (
    <Router>
      <div className="interface">
        <Topbar />
        <div className="container">
          <Sidebar />
          <Routes>
            <Route
              exact
              path="/"
              element={
                <div className="middle">
                  <InitialDashboard />
                </div>
              }
            ></Route>
            <Route
              path="/cameras"
              element={
                <div className="middle">
                  <Cameras />
                </div>
              }
            ></Route>
            <Route
              path="/alarms"
              element={
                <div className="middle">
                  <Alarms />
                </div>
              }
            ></Route>
            <Route
              path="/intrusions"
              element={
                <div className="middle">
                  <Intrusions />
                </div>
              }
            ></Route>
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default Dashboard;
