import React from "react";
import { DataGrid } from "@material-ui/data-grid";
import "./Intrusions.css";
import Popup from "reactjs-popup";
import api, {apiBaseUrl} from '../../ApiConnections/intrusion-management-api';

function Intrusions() {
  const [data, setData] = React.useState([]);

  const loadData = () => {
    api.get("/intrusion/events-triggered/1").then((res) => {
        res.data.forEach((element) => {
        element.date = element.video_date.split("T")[0];
        element.time = element.video_date.split("T")[1];
      });     
      setData(res.data);
    });
  };

  React.useEffect(() => {
    loadData();
  }, []);

  const columns = [
    {
      field: "id",
      headerName: "ID",
      width: 100,
    },
    {
      field: "building_id",
      headerName: "Building ID",
      width: 225,
    },
    {
      field: "camera_id",
      headerName: "Camera ID",
      width: 225,
    },
    {
      field: "date",
      headerName: "Date",
      sortable: false,
      width: 225,
    },
    {
      field: "time",
      headerName: "Time",
      width: 225,
    },
    {
      field: "action",
      headerName: "Action",
      width: 300,
      renderCell: (params) => {
        return (
          <div className="actions">
            <Popup
              trigger={<button className="declineBtn"> Watch Video </button>}
              modal
              nested
            >
              {(close) => (
                <div className="modal">
                  <button className="close" onClick={close}>
                    &times;
                  </button>
                  <div className="header"> Intrusion video </div>
                  <div className="player-wrapper" >
                    <video
                      id="vidObj1"
                      width="50%"
                      height="50%"
                      controls
                      loop
                      muted
                      autoplay
                      style={{position: "relative", left: "25%", top: "25%"}}
                    >
                      <source
                        // src="http://localhost:6869/intrusion-management-api/cameras/intrusions-videos/download-video.mp4"
                        src={ apiBaseUrl + "/cameras/intrusions-videos/" + params.row.id}
                        type="video/mp4"
                      />
                    </video>
                  </div>
                </div>
              )}
            </Popup>
          </div>
        );
      },
    },
  ];

  return (
    <>
      <h2 className="title">Intrusions</h2>
      <div className="userList">
        <DataGrid
          rows={data}
          columns={columns}
          disableSelectionOnClick
          pageSize={6}
          getRowId={(row) => row.id}
        />
      </div>
    </>
  );
}

export default Intrusions;
