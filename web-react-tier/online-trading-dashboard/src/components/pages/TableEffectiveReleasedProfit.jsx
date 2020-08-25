import React from 'react';
import { Table } from 'reactstrap';

const Example = (props) => {
  return (
    <>
    <h2>Released And Effective Total </h2> 
    <Table responsive>
      <thead>
        <tr>
          <th></th>
          <th>Released</th>
          <th>Effective</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Loss</th>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">Profit</th>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">Total</th>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>

      </tbody>
    </Table>
    </>
  );
}

export default Example;