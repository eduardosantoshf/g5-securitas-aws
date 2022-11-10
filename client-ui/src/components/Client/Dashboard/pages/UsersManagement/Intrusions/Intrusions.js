import React from "react";
import "./Intrusions.css";
import ReactPlayer from "react-player";

function Intrusions() {
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
