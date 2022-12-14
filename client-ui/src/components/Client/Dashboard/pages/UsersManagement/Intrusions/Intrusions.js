import React from "react";
import { useHistory } from "react-router-dom";
import { DataGrid } from "@material-ui/data-grid";
import "./Intrusions.css";
import Popup from "reactjs-popup";
import api from '../../ApiConnections/intrusion-management-api';


function Intrusions() {
  const [data, setData] = React.useState([]);

  const loadTheFuckingData = () => {
    api.get("/staff").then((res) => {
      setData(res.data);
      console.log(res.data);
    });
  };

  React.useEffect(() => {
    loadTheFuckingData();
  }, []);

  const history = useHistory();

  const data_static = [
    {
      date: "01/12/2022",
      time: "15:12:12",
      building_id: "1",
      camera_id: "123456789",
    },
    {
      date: "30/11/2022",
      time: "16:12:12",
      building_id: "1",
      camera_id: "987654321",
    },
  ];

  const columns = [
    { field: "id", headerName: "ID", width: 50 },
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
                        src="http://localhost:6869/intrusion-management-api/cameras/intrusions-videos/download-video.mp4"
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

  const handleDelete = (id) => {
    api.get(`/staff_delete/${id}`).then((res) => {
      console.log(res.affectedRows);
      setData(data.filter((item) => item.id !== id));
    });
    loadTheFuckingData();
  };

  return (
    <>
      <h2 className="title">Intrusions</h2>
      <div className="userList">
        <DataGrid
          rows={data_static}
          columns={columns}
          disableSelectionOnClick
          pageSize={6}
          getRowId={(row) => row.time}
        />
      </div>
    </>
  );
}

export default Intrusions;
