import React, {useEffect} from 'react';
import { DataGrid } from '@material-ui/data-grid';
import './Users.css';
import api from '../../ApiConnections/site-management-api';
import { useKeycloak } from "@react-keycloak/web";

function Users() {
  const { keycloak, initialized } = useKeycloak();
  const [data, setData] = React.useState([]);

  useEffect(() => {
    if (!!keycloak.authenticated) {
      console.log(keycloak.tokenParsed.sub);
      console.log(keycloak.token);
      localStorage.setItem('token_id', keycloak.tokenParsed.sub);
      localStorage.setItem('token', keycloak.token);
    }
  }, [keycloak.authenticated]);

  const loadData = () => {
    api.get('/users', {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
      setData(res.data);
      console.log(res.data);
    });
  };

  React.useEffect(() => {
    loadData();
  }, []);

  const columns = [
    { field: 'id', headerName: 'ID', width: 500 },
    {
      field: 'email',
      headerName: 'Email',
      width: 225,
    },
  ];

  return (
    <>
      <h2 className="title">Users</h2>
      <div className="userList">
        <DataGrid
          rows={data}
          columns={columns}
          disableSelectionOnClick
          pageSize={6}
          getRowId={row => row.id}
        />
      </div>

    </>
  );
}

export default Users;
