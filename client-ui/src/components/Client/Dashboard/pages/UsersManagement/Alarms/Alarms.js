import React, {useEffect, useState} from 'react';
import { DataGrid } from '@material-ui/data-grid';
import './Alarms.css';
import api from '../../ApiConnections/site-management-api';
import Select from 'react-select';
import Popup from 'reactjs-popup';
import { useKeycloak } from "@react-keycloak/web";

function Alarms() {
  const { keycloak, initialized } = useKeycloak();
  const [data, setData] = React.useState([]);
  var [buildings] = React.useState([]);
  const [property_id, setPropertyId] = React.useState(0);

  useEffect(() => {
    if (!!keycloak.authenticated) {
      localStorage.setItem('token_id', keycloak.tokenParsed.sub);
      localStorage.setItem('token', keycloak.token);
    }
  }, [keycloak.authenticated]);

  const customStyles = {
    option: (provided, state) => ({
      ...provided,
      borderBottom: '1px dotted pink',
      color: state.isSelected ? 'black' : 'black',
      padding: 20,
    }),
  }
  
  const loadData = () => {
    api.get('/users/' + localStorage.getItem('token_id') + '/alarms', {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
      setData(res.data);
    });
    api.get('/users/' + localStorage.getItem('token_id') + '/properties', {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
      (res.data).forEach(element => {
        if (buildings.find(building => building.value === element.id) === undefined) {
          buildings.push({ value: element.id, label: element.id });
        }
      });
    });
  };

  React.useEffect(() => {
    loadData();
  }, []);

  const handleDelete = id => {
    api.delete(`/alarms/${id}`, {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
      setData(data.filter(item => item.id !== id));
      loadData();
    });
  };

  const addAlarm = () => {
    api.post('alarms/?property_id=' + property_id, {}, {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
      loadData();
    });
  };

  const columns = [
    { field: 'id', headerName: 'ID', width: 50 },
    {
      field: 'id',
      headerName: 'Alarm Id',
      sortable: false,
      width: 225,
    },
    {
      field: 'property_id',
      headerName: 'Building Id',
      width: 250,
    },
    {
      field: 'is_active',
      headerName: 'Active',
      width: 250,
    },
    {
      field: 'is_alive',
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
                    Are you sure you want to remove this alarm ( {params.row.id} ) ?
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
                    <Select
                      className="select"
                      placeholder="Select Building"
                      options={buildings}
                      onChange={e => setPropertyId(e.value)}
                      styles={customStyles}
                    />
                    </div>
                  </div>
                  <div className="actions">
                    <button
                      className="declineBtn"
                      onClick={() => {
                        addAlarm();
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
          rows={data}
          disableSelectionOnClick
          columns={columns}
          pageSize={9}
          getRowId={row => row.id}
        />
      </div>
    </>
  );
}

export default Alarms;
