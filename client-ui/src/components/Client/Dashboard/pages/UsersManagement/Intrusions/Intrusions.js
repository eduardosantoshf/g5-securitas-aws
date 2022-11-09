import React from 'react';
import './Intrusions.css';
import ReactPlayer from 'react-player'

function Intrusions() {

  return (
    <>
      <h2 className="title">Intrusions</h2>
      <div className='userList' style={{display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
        <div className='player-wrapper'>
              <ReactPlayer
              className='react-player fixed-bottom'
              url= 'peopledetection.mp4'
              width='50%'
              height='50%'
              controls = {true}

              />
          </div>
          <div className='player-wrapper'>
              <ReactPlayer
              className='react-player fixed-bottom'
              url= 'peopledetection.mp4'
              width='50%'
              height='50%'
              controls = {true}

              />
          </div>
      </div>
    </>
  );
}

export default Intrusions;
