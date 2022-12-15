import React from "react";
import "./Sidebar.css";
import { useKeycloak } from "@react-keycloak/web";

import { useNavigate } from "react-router-dom";

import PeopleRoundedIcon from "@material-ui/icons/PeopleRounded";
import TreeRounded from "@material-ui/icons/AccountTreeRounded";
import DashboardOut from "@material-ui/icons/BarChartRounded";
import Camera from "@material-ui/icons/Camera";
import Alarm from "@material-ui/icons/Alarm";
import Video from "@material-ui/icons/VideoLibrary";

import { slide as Menu } from "react-burger-menu";

function Sidebar() {
  const { keycloak, initialized } = useKeycloak();
  let navigate = useNavigate();

  const initDashboard = () => {
    navigate("/");
  };

  const cameras = () => {
    navigate("/cameras");
  };

  const alarms = () => {
    navigate("/alarms");
  };

  const intrusions = () => {
    navigate("/intrusions");
  };

  if (!!keycloak.authenticated) {
    return (
      <Menu>
        <a className="menu-item" onClick={initDashboard}>
          <span className="lefti">Dashboard </span>
          <span className="righti">
            <DashboardOut />
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
        <a className="menu-item" onClick={intrusions}>
          <span className="lefti">Intrusions </span>
          <span className="righti">
            <Video />
          </span>
        </a>
      </Menu>
    );
  }

  return (
    <Menu>
      <a className="menu-item" onClick={initDashboard}>
        <span className="lefti">Dashboard </span>
        <span className="righti">
          <DashboardOut />
        </span>
      </a>
    </Menu>
  );
}

export default Sidebar;
