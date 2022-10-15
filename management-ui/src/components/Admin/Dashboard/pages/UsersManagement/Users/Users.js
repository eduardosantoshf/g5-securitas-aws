import React from 'react';
import { useHistory } from 'react-router-dom';
import { DataGrid } from '@material-ui/data-grid';
import './Users.css';
import Popup from 'reactjs-popup';
import api from '../../ApiConnections/apiManageAccess';

function Users() {
  const [data, setData] = React.useState([]);

  const loadTheFuckingData = () => {
    api.get('/staff').then(res => {
      setData(res.data);
      console.log(res.data);
    });
  };

  React.useEffect(() => {
    loadTheFuckingData();
  }, []);

  const history = useHistory();

  const columns = [
    { field: 'id', headerName: 'ID', width: 50 },
    {
      field: 'fullname',
      headerName: 'Full Name',
      sortable: false,
      width: 225,
    },
    /*
    {
      field: 'hospital',
      headerName: 'Hospital',
      width: 250,
    },
    {
      field: 'professional_id',
      headerName: 'License Number',
      width: 200,
    },
    */
    {
      field: 'email',
      headerName: 'Email',
      width: 225,
    },
    /*
    {
      field: 'type_user',
      headerName: 'Job',
      width: 225,
    },*/
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
                    Are you sure you want to eliminate this user?
                  </div>
                  <div className="actions">
                    <button
                      className="declineBtn"
                      onClick={() => {
                        handleDelete(params.row.email);
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
    api.get(`/staff_delete/${id}`).then(res => {
      console.log(res.affectedRows);
      setData(data.filter(item => item.id !== id));
    });
    loadTheFuckingData();
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
                      <div style={{float:"left"}}>
                        <label for="fname">Full Name</label>
                      </div>
                      <div >
                        <input type="text" id="fname" name="fullname" placeholder="Full Name"/>
                      </div>
                      <div style={{float:"left"}}>
                        <label for="fname">Email</label>
                      </div>
                      <div >
                        <input type="text" id="email" name="email" placeholder="Email"/>
                      </div>
                  </div>
                  <div className="actions">
                    <button
                      className="declineBtn"
                      onClick={() => {
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
