import React from "react";
import "./Intrusions.css";

function Intrusions() {
  /*
  React.useEffect(() => {
    console.log("Intrusions.js: useEffect() called");
    api.get("/cameras/intrusions-videos").then((res) => {
      var myUrl = (window.URL || window.webkitURL).createObjectURL(
        new Blob([res.data])
      ); // response.data.data

      var myVid = document.getElementById("vidObj");
      myVid.setAttribute("src", myUrl);
      myVid.play(); //# test playback
      console.log("ACABOU");

      //setVideo(url); //# is this needed?
    });
    console.log("ACABOU");
  });
  */
  return (
    <>
      <h2 className="title">Intrusions</h2>
      <div
        className="userList"
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <div className="player-wrapper">
          <video
            id="vidObj"
            width="50%"
            height="50%"
            controls
            loop
            muted
            autoplay
          >
            <source
              src="http://localhost:8000/cameras/intrusions-videos"
              type="video/mp4"
            />
          </video>
        </div>
        <div className="player-wrapper">
        <video
            id="vidObj"
            width="50%"
            height="50%"
            controls
            loop
            muted
            autoplay
          >
            <source
              src="http://localhost:8000/cameras/intrusions-videos"
              type="video/mp4"
            />
          </video>
        </div>
      </div>
    </>
  );
}

export default Intrusions;
