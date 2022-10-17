import React, { Component } from 'react';
import './Dashboard.css';
import Sidebar from './nestedComponents/Sidebar';
import Topbar from './nestedComponents/Topbar';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Cameras from './pages/UsersManagement/Cameras/Cameras';
import InitialDashboard from './pages/UsersManagement/InitialDashboard/InitialDashboard';
import Users from './pages/UsersManagement/Users/Users';
import Nodes from './pages/UsersManagement/DicomNodes/Nodes';
import ExtensionInstall from './pages/UsersManagement/ExtensionInstall/ExtensionInstall';
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
            <Route path="/cameras">
              <div className="middle">
                <Cameras />
              </div>
            </Route>
            <Route path="/users">
              <div className="middle">
                <Users />
              </div>
            </Route>
            <Route path="/nodes">
              <div className="middle">
                <Nodes />
              </div>
            </Route>
            <Route path="/extInstallation">
              <div className="middle">
                <ExtensionInstall />
              </div>
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default Dashboard;
