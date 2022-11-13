import React from "react";
import "./Sidebar.css";

import { useHistory } from "react-router-dom";

import PeopleRoundedIcon from "@material-ui/icons/PeopleRounded";
import TreeRounded from "@material-ui/icons/AccountTreeRounded";
import DashboardOut from "@material-ui/icons/BarChartRounded";
import Camera from '@material-ui/icons/Camera';
import Alarm from '@material-ui/icons/Alarm';
import Video from '@material-ui/icons/VideoLibrary';

import { slide as Menu } from "react-burger-menu";

function Sidebar() {
  const history = useHistory();

  const initDashboard = () => {
    history.push("/");
  };

  const cameras = () => {
    history.push("/cameras");
  };

  const alarms = () => {
    history.push("/alarms");
  };

  const intrusions = () => {
    history.push("/intrusions");
  };


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

export default Sidebar;
