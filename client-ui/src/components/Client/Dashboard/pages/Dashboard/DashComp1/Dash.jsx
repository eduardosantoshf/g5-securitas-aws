import React from 'react';
import './dash.css';
import PeopleIcon from '@material-ui/icons/People';
import Filter9PlusIcon from '@material-ui/icons/Filter9Plus';
import ViewModuleIcon from '@material-ui/icons/ViewModule';
import SaveIcon from '@material-ui/icons//Save';
import api from '../../ApiConnections/api';

export default function Dash() {
  const [data_stats, setData] = React.useState([]);

  React.useEffect(() => {
    api.get('/statistics').then(res => {
      setData(res.data);
      console.log(res);
    });
  }, []);

  return (
    <div className="dash">
      <div className="dashItem">
        <div className="part1">
          <span className="dashTitle">Frames analized</span>
          <div className="dashInstancesContainer">
            <span className="dashInstances">{data_stats.CountInstances}</span>
            <span className="dashInstances">{123421}</span>
          </div>
        </div>
        <div className="dashIcons">
          <Filter9PlusIcon fontSize="large" />
        </div>
      </div>

      <div className="dashItem">
        <div className="part1">
          <span className="dashTitle">Clients</span>
          <div className="dashInstancesContainer">
            <span className="dashInstances">{data_stats.CountPatients}</span>
            <span className="dashInstances">{12}</span>
          </div>
        </div>
        <div className="dashIcons">
          <PeopleIcon fontSize="large" />
        </div>
      </div>

      <div className="dashItem">
        <div className="part1">
          <span className="dashTitle"></span>
          <div className="dashInstancesContainer">
            <span className="dashInstances"> {data_stats.CountSeries}</span>
            <span className="dashInstances"> {data_stats.CountSeries}</span>
          </div>
        </div>
        <div className="dashIcons">
          <ViewModuleIcon fontSize="large" />
        </div>
      </div>

      <div className="dashItem">
        <div className="part1">
          <span className="dashTitle"></span>
          <div className="dashInstancesContainer">
            <span className="dashInstances">{data_stats.TotalDiskSizeMB}</span>
            <span className="dashInstances">{data_stats.TotalDiskSizeMB}</span>
          </div>
        </div>
        <div className="dashIcons">
          <SaveIcon fontSize="large" />
        </div>
      </div>
    </div>
  );
}
