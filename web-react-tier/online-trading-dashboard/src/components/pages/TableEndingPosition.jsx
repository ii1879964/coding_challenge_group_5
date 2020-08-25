import React from 'react';
import { Table } from 'reactstrap';

const Example = (props) => {
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
        <tr>
          <th scope="row">1</th>
          <td>Astronomica</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Borealis </td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td>Celestial</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">4</th>
          <td>Deuteronic</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">5</th>
          <td>Eclipse</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">6</th>
          <td>Floral</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">7</th>
          <td>Galactia</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">8</th>
          <td>Heliosphere</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">9</th>
          <td>Interstella</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
        <tr>
          <th scope="row">10</th>
          <td>Jupiter</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>        <tr>
          <th scope="row">11</th>
          <td>Koronis</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
         <tr>
          <th scope="row">12</th>
          <td>Lunatic</td>
          <td>Table cell</td>
          <td>Table cell</td>
        </tr>
      </tbody>
    </Table>
    </>
  );
}

export default Example;