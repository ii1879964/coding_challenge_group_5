import React from 'react';
import { Table } from 'reactstrap';

const Example = (props) => {
  const { array } = props;

  const table = array ? array.map((row, index) => {
    const {name, prices}= row;
    return <tr key={name+index+"position"}>
            <th scope="row">{index+1}</th>
            <td>{name}</td>
            <td>{prices.buy}</td>
            <td>{prices.sell}</td>
          </tr>
  }) : null;

  return (
    <>
    <h2>My Ending Position</h2>
    <Table responsive>
      <thead>
        <tr>
          <th>#</th>
          <th>Instruments</th>
          <th>Long Position</th>
          <th>Short Position</th>
        </tr>
      </thead>
      <tbody>
        {table}
      </tbody>
    </Table>
    </>
  );
}

export default Example;