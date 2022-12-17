import React from 'react';
import './Topbar.css';
import { useKeycloak } from "@react-keycloak/web";
import PersonOutlineRoundedIcon from '@material-ui/icons/PersonOutlineRounded';

const handleLogout = () => {
  localStorage.removeItem('token');
  window.location.href = 'http://localhost:3000';
  localStorage.removeItem('user');
  localStorage.removeItem('type_user');
};

function Topbar() {
  const { keycloak, initialized } = useKeycloak();
  return (
    <div className="topbar">
      <div className="topbarWrapper">
        <div className="topLeft">
          <div className="logo">G5 Securitas</div>
        </div>
        <div className="topRigth">
        {!keycloak.authenticated && (
            <div className="icons" onClick={() => keycloak.login()}>
              Login
            </div>
          )}
          {!!keycloak.authenticated && (
            <div className="icons" onClick={() => keycloak.logout()}>
              Logout
              <PersonOutlineRoundedIcon />(
              {keycloak.tokenParsed.preferred_username})
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Topbar;
