import React, { Component } from 'react';
import './Dashboard.css';
import Sidebar from './nestedComponents/Sidebar';
import Topbar from './nestedComponents/Topbar';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Cameras from './pages/UsersManagement/Cameras/Cameras';
import InitialDashboard from './pages/UsersManagement/InitialDashboard/InitialDashboard';
import Alarms from "./pages/UsersManagement/Alarms/Alarms";
import Properties from "./pages/UsersManagement/Properties/Properties";
import Users from './pages/UsersManagement/Users/Users';
function Dashboard() {
  return (
    <Router>
      <div className="interface">
        <Topbar />
        <div className="container">
          <Sidebar />
          <Switch>
            <Route exact path="/">
              <div className="middle">
                <InitialDashboard />
              </div>
            </Route>
            <Route path="/properties">
              <div className="middle">
                <Properties />
              </div>
            </Route>
            <Route path="/cameras">
              <div className="middle">
                <Cameras />
              </div>
            </Route>
            <Route path="/alarms">
              <div className="middle">
                <Alarms />
              </div>
            </Route>
            <Route path="/users">
              <div className="middle">
                <Users />
              </div>
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default Dashboard;
