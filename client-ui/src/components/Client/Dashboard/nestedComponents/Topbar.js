import React, {useEffect} from "react";
import "./Topbar.css";
import { useKeycloak } from "@react-keycloak/web";

import PersonOutlineRoundedIcon from "@material-ui/icons/PersonOutlineRounded";

function Topbar() {
  const { keycloak, initialized } = useKeycloak();

  // useEffect(() => {
  //   keycloak.init({ onLoad: 'login-required' }).then(authenticated => {
  //     if (!authenticated) {
  //       keycloak.login();
  //     }
  //   });
  // }, []);


  return (
    <div className="topbar">
      <div className="topbarWrapper">
        <div className="topLeft">
          <div className="logo">G5 Securitas</div>
        </div>
        <div className="topRigth">
          {!keycloak.authenticated && (
            <div
              className="icons"
              onClick={() => {

                keycloak.login()
                .then(() => {
                  // The request to the token endpoint was successful
                  console.log(keycloak.token)
                })
                .catch(error => {
                  // There was an error with the request to the token endpoint
                  console.log(error)
                });
              }}
            >
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
