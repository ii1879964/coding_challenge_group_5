import React, { Component } from 'react';
import { Table } from 'reactstrap';

export default class TabelHistoricData extends Component {
    render() {
        const { data } = this.props;

        const table = data ? data.map((row, index) => {
            return <tr key={row.deal_time+" "+index}>
                        <td>{row.counterparty_name}</td>
                        <td>{row.instrument_name}</td>
                        <td>{row.deal_type}</td>
                        <td>{row.deal_quantity}</td>
                        <td>{row.deal_price}</td>
                        <td>{row.deal_time}</td>
                    </tr>
        }) : null;


        return (
            <div className="historic-data">
                <h2>Historical data</h2>
                <Table striped>
                    <thead>
                        <tr>
                            <th>Counterparty</th>
                            <th>Instrument</th>
                            <th>Type</th>
                            <th>Quantity</th>
                            <th>Price</th>
                            <th>Time</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table}
                    </tbody>
                    </Table>
            </div>
        );
    }
}