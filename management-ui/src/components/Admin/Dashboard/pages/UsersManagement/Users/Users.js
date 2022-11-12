import React from 'react';
import { DataGrid } from '@material-ui/data-grid';
import './Users.css';
import Popup from 'reactjs-popup';
import api from '../../ApiConnections/site-management-api';

import moment from 'moment'


function Users() {
  const [data, setData] = React.useState([]);

  const [name, setName] = React.useState('');
  const [email, setEmail] = React.useState('');
  const [address, setAddress] = React.useState('');

  const loadData = () => {
    api.get('/users').then(res => {
      setData(res.data);
      console.log(res.data);
    });
  };

  const addUser = () => {
    const created_at = moment().format('YYYY-MM-DD');
    const user = { "name": name, "email": email, "address": address, "created_at": created_at };
    api.post('/users', user).then(res => {
      console.log(res.data);
      loadData();
    });
  };

  React.useEffect(() => {
    loadData();
  }, []);


  const columns = [
    { field: 'id', headerName: 'ID', width: 50 },
    {
      field: 'name',
      headerName: 'Name',
      sortable: false,
      width: 225,
    },
    {
      field: 'email',
      headerName: 'Email',
      width: 225,
    },
    {
      field: 'address',
      headerName: 'Address',
      width: 350,
    },
    {
      field: 'action',
      headerName: 'Action',
      width: 300,
      renderCell: params => {
        return (
          <div className="actions">
            <Popup
              trigger={<button className="declineBtn"> Eliminate </button>}
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
                    Are you sure you want to eliminate this user ( {params.row.email} ) ?
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

  const handleDelete = id => {
    api.delete(`/users/${id}`).then(res => {
      console.log(res.affectedRows);
      setData(data.filter(item => item.id !== id));
      loadData();
    });
  };

  return (
    <>
      <h2 className="title">Users</h2>
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
                  <div className="header"> Add User </div>
                  <div className="header" style={{ color: "white", borderBottomWidth: 0 }}>
                    <div style={{display:"flex", justifyContent:"space-around"}}>
                       <div style={{ width:"100px", textAlign: "left"}}>
                        <label style={{width:"40px"}} for="fname">Name</label>
                      </div>
                    <input
                      style={{ width: "45%" }}
                      type="text" id="fname"
                      name="name"
                      placeholder="Name"
                      onChange={e => setName(e.target.value)}
                    />
                    </div>
                    <div style={{display:"flex", justifyContent:"space-around"}}>
                      <div style={{ width:"100px", textAlign: "left"}}>
                        <label for="fname">Email</label>
                      </div>
                    <input
                      style={{ width: "45%" }}
                      type="text"
                      id="email"
                      name="email"
                      placeholder="Email"
                      onChange={e => setEmail(e.target.value)}
                    />
                  </div>
                  <div style={{display:"flex", justifyContent:"space-around"}}>
                      <div style={{ width:"100px", textAlign: "left"}}>
                        <label for="fname">Address</label>
                      </div>
                    <input
                      style={{ width: "45%" }}
                      type="text"
                      id="address"
                      name="address"
                      placeholder="Address"
                      onChange={e => setAddress(e.target.value)}
                    />
                    </div>
                  </div>
                  <div className="actions">
                    <button
                      className="declineBtn"
                      onClick={() => {
                        addUser();
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
          columns={columns}
          disableSelectionOnClick
          pageSize={6}
          getRowId={row => row.email}
        />
      </div>

    </>
  );
}

export default Users;
