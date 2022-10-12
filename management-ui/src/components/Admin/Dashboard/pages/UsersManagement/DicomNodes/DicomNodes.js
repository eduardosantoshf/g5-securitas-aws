import React from 'react';
import Cytoscape from 'cytoscape';
import CytoscapeComponent from 'react-cytoscapejs';
import COSEBilkent from 'cytoscape-cose-bilkent';

Cytoscape.use(COSEBilkent);

export default class DicomNodes extends React.Component {
  initListeners() {
    this.cy.on('tap', 'node', evt => {
      var node = evt.target;
      console.log(node.data());
      document.getElementById('label').innerHTML = node.data().label;
      document.getElementById(
        'description'
      ).innerHTML = node.data().description;
    });
  }
  componentWillUnmount() {
    console.log('remove listeners');
    if (this.cy) {
      this.cy.removeAllListeners();
    }
  }
  render() {
    const elements = [
      {
        data: {
          id: 'one',
          label: 'Camera-1',
          description: 'Samsung Camera',
        },
        style: { color: 'SkyBlue', 'font-size': '10px' },
      },
      {
        data: {
          id: 'two',
          label: 'Client 123123',
          type: 'comp',
          description: 'Cliente number 123123',
        },
        style: { color: 'SkyBlue', 'font-size': '10px' },
      },
      {
        data: {
          id: 'three',
          label: 'Camera-2',
          description: 'Sony Camera',
        },
        style: { color: 'SkyBlue', 'font-size': '10px' },
      },
      {
        data: {
          id: 'four',
          label: 'Camera-3',
          description: 'Canon Camera',
        },
        style: { color: 'SkyBlue', 'font-size': '10px' },
      },
      {
        data: {
          source: 'one',
          target: 'two',
          label: 'Edge from Node1 to Node2',
        },
      },
      {
        data: {
          source: 'three',
          target: 'two',
          label: 'Edge from Node1 to Node2',
        },
      },
      {
        data: {
          source: 'four',
          target: 'two',
          label: 'Edge from Node1 to Node2',
        },
      },
    ];

    const layout = { name: 'cose-bilkent' };

    return (
      <CytoscapeComponent
        elements={elements}
        layout={layout}
        cy={cy => {
          this.cy = cy;
          this.initListeners();
        }}
        stylesheet={[
          {
            selector: 'node',
            style: {
              'background-color': '#282',
              label: 'data(label)',
              //opacity: 0.3
            },
          },
          {
            selector: 'node[type="comp"]',
            style: {
              'background-color': '#822',
            },
          },
          {
            selector: 'edge',
            style: {
              width: 2,
              'line-color': '#ffffff',
              'target-arrow-color': '#ccc',
              'target-arrow-shape': 'triangle',
              'curve-style': 'bezier',
            },
          },
        ]}
        style={{
          width: '300px',
          height: '600px',
          display: 'flex',
          flex: 3,
        }}
      />
    );
  }
}
