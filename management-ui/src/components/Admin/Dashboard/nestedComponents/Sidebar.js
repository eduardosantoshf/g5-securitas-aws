import React from "react";
import "./Sidebar.css";

import { useHistory } from "react-router-dom";

import PeopleRoundedIcon from "@material-ui/icons/PeopleRounded";
import TreeRounded from "@material-ui/icons/AccountTreeRounded";
import DashboardOut from "@material-ui/icons/BarChartRounded";
import Camera from '@material-ui/icons/Camera';

import { slide as Menu } from "react-burger-menu";

function Sidebar() {
  const history = useHistory();

  const initDashboard = () => {
    history.push("/");
  };

  const cameras = () => {
    history.push("/cameras");
  };

  const nodes = () => {
    history.push("/nodes");
  };

  const users = () => {
    history.push("/users");
  };


  return (
    <Menu>
      <a className="menu-item" onClick={initDashboard}>
        <span className="lefti">Dashboard </span>
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
      <a className="menu-item" onClick={cameras}>
        <span className="lefti">List Cameras </span>
        <span className="righti">
          <Camera />
        </span>
      </a>
      <a className="menu-item" onClick={nodes}>
        <span className="lefti">Camera Nodes </span>
        <span className="righti">
          <TreeRounded />
        </span>
      </a>
    </Menu>
  );
}

export default Sidebar;
