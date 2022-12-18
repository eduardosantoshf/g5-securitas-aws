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
            <Route exact path="/admin/">
              <div className="middle">
                <InitialDashboard />
              </div>
            </Route>
            <Route path="/admin/properties">
              <div className="middle">
                <Properties />
              </div>
            </Route>
            <Route path="/admin/cameras">
              <div className="middle">
                <Cameras />
              </div>
            </Route>
            <Route path="/admin/alarms">
              <div className="middle">
                <Alarms />
              </div>
            </Route>
            <Route path="/admin/users">
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
