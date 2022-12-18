import React, {useEffect} from 'react';
import { DataGrid } from '@material-ui/data-grid';
import './Properties.css';
import api from '../../ApiConnections/site-management-api';
import { useKeycloak } from "@react-keycloak/web";
import Select from 'react-select';

import Popup from 'reactjs-popup';

function Properties() {
  const { keycloak, initialized } = useKeycloak();
  const [data, setData] = React.useState([]);
  // var [users_ids] = React.useState([]);
  // const [owner_id, setPropertyId] = React.useState(0);

  useEffect(() => {
    if (!!keycloak.authenticated) {
      console.log(keycloak.tokenParsed.sub);
      console.log(keycloak.token);
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
    console.log(localStorage.getItem('token_id'))
    console.log(localStorage.getItem('token'))
    // api.get('/users/1/properties').then(res => {
    api.get('/properties', {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
      setData(res.data);
      console.log(res.data);
    });
    // api.get('/users', {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
    //   console.log(res.data);
    //   (res.data).forEach(element => {
    //     if (users_ids.find(user => user.id === element.id) === undefined) {
    //       users_ids.push({ value: element.id, label: element.id });
    //     }
    //   });
    //   console.log(users_ids);
    // });
  };

  React.useEffect(() => {
    loadData();
  }, []);

  // const handleDelete = id => {
  //   api.delete(`/properties/${id}`, {headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
  //     console.log(res.affectedRows);
  //     setData(data.filter(item => item.id !== id));
  //     loadData();
  //   });
  // };

  // const addProperty = () => {
  //   api.post('properties/?owner_id=' + owner_id, {},{headers:{'Authorization': `Bearer ${localStorage.getItem('token')}`}}).then(res => {
  //     console.log(res.data);
  //     loadData();
  //   });
  // };

  const columns = [
    {
      field: 'id',
      headerName: 'Property Id',
      sortable: false,
      width: 150,
    },
    {
      field: 'address',
      headerName: 'Address',
      width: 250,
    },
    {
      field: 'owner_id',
      headerName: 'Owner Id',
      width: 350,
    },
    // {
    //   field: 'action',
    //   headerName: 'Action',
    //   width: 300,
    //   renderCell: params => {
    //     return (
    //       <div className="actions">
    //         <Popup
    //           trigger={<button className="declineBtn"> Remove </button>}
    //           modal
    //           nested
    //         >
    //           {close => (
    //             <div className="modal">
    //               <button className="close" onClick={close}>
    //                 &times;
    //               </button>
    //               <div className="header"> Confirmation - Elimination </div>
    //               <div className="header" style={{ color: "white" , align: "center", borderBottomWidth: 0 }}>
    //                 {' '}
    //                 Are you sure you want to remove this property ( {params.row.id} ) ?
    //               </div>
    //               <div className="actions">
    //                 <button
    //                   className="declineBtn"
    //                   onClick={() => {
    //                     handleDelete(params.row.id);
    //                     close();
    //                   }}
    //                 >
    //                   Yes
    //                 </button>
    //                 <button
    //                   className="acceptBtn"
    //                   onClick={() => {
    //                     close();
    //                   }}
    //                 >
    //                   No
    //                 </button>
    //               </div>
    //             </div>
    //           )}
    //         </Popup>
    //       </div>
    //     );
    //   },
    // },
  ];

  return (
    <>
      <h2 className="title">Properties</h2>
      {/* <div className="btns-wrapper">
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
                  <div className="header"> Add Property </div>
                  <div className="header" style={{ color: "white", borderBottomWidth: 0 }}>
                    <div style={{display:"flex", justifyContent:"space-around"}}>
                       <div style={{ width:"100px", textAlign: "left"}}>
                        <label style={{width:"40px"}} for="fname">Building</label>
                      </div>
                      <Select
                      className="select"
                      placeholder="Select Building"
                      options={users_ids}
                      onChange={e => setPropertyId(e.value)}
                      styles={customStyles}
                    />
                    </div>
                  </div>
                  <div className="actions">
                    <button
                      className="declineBtn"
                      onClick={() => {
                        addProperty();
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
      </div> */}
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

export default Properties;
