import React from 'react';
import './chart.css';
import { Chart as ChartJS, registerables } from 'chart.js';
import { Line } from 'react-chartjs-2';
import api from '../../ApiConnections/apiManageAccess';
ChartJS.register(...registerables);

//TODO: https://stackoverflow.com/questions/51508665/using-data-from-api-with-chart-js
//TODO: Ver cenas no link acima, para ver como se faz isso dinamico, e fazer uma querie a base de dados, com os ultimos x dias/meses whatever do que for, e mostrar no grafico

export default function Chart() {
  const [data, setData] = React.useState([]);


  React.useEffect(() => {
      api.get('/chart_dash').then(res => {
        setData(res.data);
        console.log(res.data);
      });
  }, []);
  
  
  const state = {
    labels: data.map(d => d.day_),
    datasets: [
      {
        label: 'gráfico',
        fill: true,
        lineTension: 0.5,
        backgroundColor: 'rgba(75,192,192,1)',
        borderColor: 'rgba(0,0,0,1)',
        borderWidth: 2,
        data: data.map(d => d.count_studies),
      },
    ],
  };

/*
<Line
  data={state}
  options={{
    title: {
      display: false,
      text: 'Average Rainfall per month',
      fontSize: 20,
    },
    legend: {
      display: true,
      position: 'right',
    },
  }}
/>
*/ 

  return (
    <div className="chart">
      <div className="chartItem">

        <Line
          color='red'
          backgroundColor='red'
          datasetIdKey='id'
          data={{
            labels: ['Jun', 'Jul', 'Aug'],
            datasets: [
              {
                id: 1,
                label: 'Dataset 1',
                data: [5, 6, 7],
                backgroundColor: '#FFFFFF',
                borderColor: '#FFFFFF',
              },
              {
                id: 2,
                label: 'Dataset 2',
                data: [3, 2, 1],
                borderColor: '#FFFFFF',

              },
            ],
          }}
        />
      </div>
    </div>
  );
}
