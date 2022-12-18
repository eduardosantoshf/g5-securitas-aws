import React, { useEffect } from "react";
import "./Topbar.css";
import { useKeycloak } from "@react-keycloak/web";

import PersonOutlineRoundedIcon from "@material-ui/icons/PersonOutlineRounded";

function Topbar() {
  const { keycloak, initialized } = useKeycloak();

  useEffect(() => {
    if (!!keycloak.authenticated) {
      localStorage.setItem("token_id", keycloak.tokenParsed.sub);
      localStorage.setItem("token", keycloak.token);
    }
  }, [keycloak.authenticated]);

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
                keycloak
                  .login()
                  .then(() => {
                    // The request to the token endpoint was successful
                    console.log("success");
                  })
                  .catch((error) => {
                    // There was an error with the request to the token endpoint
                    console.log("error");
                    console.log(error);
                  });
              }}
            >
              Login
            </div>
          )}
          {!!keycloak.authenticated && (
            <div
              className="icons"
              onClick={() => {
                keycloak.logout();
                window.location.href = "/";
                localStorage.removeItem("token_id");
                localStorage.removeItem("token");
              }}
            >
              Logout
              <PersonOutlineRoundedIcon />({keycloak.tokenParsed.given_name})
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Topbar;
