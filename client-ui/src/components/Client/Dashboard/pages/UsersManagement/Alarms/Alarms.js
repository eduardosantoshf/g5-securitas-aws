import React from 'react';
import { DataGrid } from '@material-ui/data-grid';
import { useHistory } from 'react-router-dom';
import './Alarms.css';
import api from '../../ApiConnections/apiManageAccess';

import Popup from 'reactjs-popup';

function Alarms() {
  const [data, setData] = React.useState([]);

  const loadTheFuckingData = () => {
    api.get('/request_account').then(res => {
      setData(res.data);
      console.log(res.data);
    });
  };

  React.useEffect(() => {
    loadTheFuckingData();
  }, []);

  const history = useHistory();

  const initDashboard = () => {
    history.push('/users');
  };

  const handleDelete = id => {
    api.get(`/request_delete/${id}`).then(res => {
      loadTheFuckingData();
    });
  };

  const handleAccept = id => {
    api.get(`/request_accept/${id}`).then(res => {
      console.log(res.affectedRows);
      setData(data.filter(item => item.id !== id));
    });
    api.get(`/request_accepte_update/${id}`).then(res => {
      console.log(res.affectedRows);
      setData(data.filter(item => item.id !== id));
    });
    loadTheFuckingData();
  };

  const data_static = [
    {
      alarm_id: "132421543",
      building_id: 'build1',
      active: 'yes',
      alive: 'yes',
    },
    {
      alarm_id: "125754345",
      building_id: 'build1',
      active: 'yes',
      alive: 'no',
    }
  ]

  const columns = [
    { field: 'id', headerName: 'ID', width: 50 },
    {
      field: 'alarm_id',
      headerName: 'Alarm Id',
      sortable: false,
      width: 225,
    },
    {
      field: 'building_id',
      headerName: 'Building Id',
      width: 250,
    },
    {
      field: 'active',
      headerName: 'Active',
      width: 250,
    },
    {
      field: 'alive',
      headerName: 'Alive',
      width: 250,
    },
    {
      field: 'action',
      headerName: 'Action',
      width: 300,
      renderCell: params => {
        return (
          <div className="actions">
            <Popup
              trigger={<button className="declineBtn"> Remove </button>}
              modal
              nested
            >
              {close => (
                <div className="modal">
                  <button className="close" onClick={close}>
                    &times;
                  </button>
                  <div className="header"> Confirmation - Elimination </div>
                  <div className="header" style={{ color: "white" , align: "center", borderBottomWidth: 0 }}>
                    {' '}
                    Are you sure you want to remove this alarm ( {params.row.alarm_id} ) ?
                  </div>
                  <div className="actions">
                    <button
                      className="declineBtn"
                      onClick={() => {
                        handleDelete(params.row.id);
                        close();
                      }}
                    >
                      Yes
                    </button>
                    <button
                      className="acceptBtn"
                      onClick={() => {
                        close();
                      }}
                    >
                      No
                    </button>
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
      <h2 className="title">Alarms</h2>
      <div className="btns-wrapper">
        <div className="btns">
        <Popup
              trigger={<button className="request"> Add </button>}
              modal
              nested
            >
              {close => (
                <div className="modal">
                  <button className="close" onClick={close}>
                    &times;
                  </button>
                  <div className="header"> Add Alarm </div>
                  <div className="header" style={{ color: "white", borderBottomWidth: 0 }}>
                    <div style={{display:"flex", justifyContent:"space-around"}}>
                       <div style={{ width:"100px", textAlign: "left"}}>
                        <label style={{width:"40px"}} for="fname">Building</label>
                      </div>
                    <input
                      style={{ width: "45%" }}
                      type="text" id="fname"
                      name="name"
                      placeholder="Name"
                      //</input>onChange={e => setName(e.target.value)}
                    />
                    </div>
                  </div>
                  <div className="actions">
                    <button
                      className="declineBtn"
                      onClick={() => {
                        //addUser();
                        close();
                      }}
                    >
                      Create
                    </button>
                    <button
                      className="acceptBtn"
                      onClick={() => {
                        close();
                      }}
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              )}
            </Popup>
        </div>
      </div>
      <div className="userList">
        <DataGrid
          rows={data_static}
          disableSelectionOnClick
          columns={columns}
          pageSize={9}
          getRowId={row => row.alarm_id}
        />
      </div>
    </>
  );
}

export default Alarms;
