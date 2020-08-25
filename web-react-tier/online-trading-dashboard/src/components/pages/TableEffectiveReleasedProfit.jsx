import React from 'react';
import { Table } from 'reactstrap';

const TableEffectiveReleasedProfit = (props) => {
  const {realizedBalance, effectiveBalance} = props;

  return (
    <div className="profit-table">
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
            <td>{realizedBalance ? realizedBalance.loss : "loading"}</td>
            <td>{effectiveBalance ? effectiveBalance.loss : "loading"}</td>
          </tr>
          <tr>
            <th scope="row">Profit</th>
            <td>{realizedBalance ? realizedBalance.profit : "loading"}</td>
            <td>{effectiveBalance ? effectiveBalance.profit : "loading"}</td>
          </tr>
          <tr>
            <th scope="row">Total</th>
            <td>{realizedBalance ? realizedBalance.sum : "loading"}</td>
            <td>{effectiveBalance ? effectiveBalance.sum : "loading"}</td>
          </tr>

        </tbody>
      </Table>
    </div>
  );
}

export default TableEffectiveReleasedProfit;