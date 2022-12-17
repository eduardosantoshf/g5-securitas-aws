import React from "react";
import "./Sidebar.css";
import { useKeycloak } from "@react-keycloak/web";

import { useHistory } from "react-router-dom";

import PeopleRoundedIcon from "@material-ui/icons/PeopleRounded";
import DashboardOut from "@material-ui/icons/Home";
import Camera from "@material-ui/icons/Camera";
import Property from "@material-ui/icons/Domain";
import Alarm from "@material-ui/icons/Alarm";

import { slide as Menu } from "react-burger-menu";

function Sidebar() {
  const { keycloak, initialized } = useKeycloak();
  const history = useHistory();

  const initDashboard = () => {
    history.push("/");
  };

  const cameras = () => {
    history.push("/cameras");
  };

  const properties = () => {
    history.push("/properties");
  };

  const alarms = () => {
    history.push("/alarms");
  };

  const users = () => {
    history.push("/users");
  };

  if (!!keycloak.authenticated) {
    return (
      <Menu>
        <a className="menu-item" onClick={initDashboard}>
          <span className="lefti">Home </span>
          <span className="righti">
            <DashboardOut />
          </span>
        </a>
        <a className="menu-item" onClick={users}>
          <span className="lefti">Users </span>
          <span className="righti">
            <PeopleRoundedIcon />
          </span>
        </a>
        <a className="menu-item" onClick={properties}>
          <span className="lefti">Properties </span>
          <span className="righti">
            <Property />
          </span>
        </a>
        <a className="menu-item" onClick={cameras}>
          <span className="lefti">Cameras </span>
          <span className="righti">
            <Camera />
          </span>
        </a>
        <a className="menu-item" onClick={alarms}>
          <span className="lefti">Alarms </span>
          <span className="righti">
            <Alarm />
          </span>
        </a>
      </Menu>
    );
  }

  return (
    <Menu>
      <a className="menu-item" onClick={initDashboard}>
        <span className="lefti">Home </span>
        <span className="righti">
          <DashboardOut />
        </span>
      </a>
    </Menu>
  );
}

export default Sidebar;
