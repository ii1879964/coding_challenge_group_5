import React, {Component} from 'react';
import HistogramAverageBuySell from '../pages/HistogramAverageBuySell'
import AlertDB from '../pages/AlertDB'
import TableEndingPosition from '../pages/TableEndingPosition'
import TableEffectiveReleasedProfit from '../pages/TableEffectiveReleasedProfit'
import { Button } from 'reactstrap';

export default class Dashboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            IsConnectedDataBase : true
        }
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.history.push("/");
    }

    render(){
        const { connectionStatus } = this.props;

        const content = connectionStatus  ? "" : <AlertDB></AlertDB>;

        return (
            <div>
                <h1>Online Trading Dashboard</h1>
                <p><Button onClick = {this.handleSubmit} color="primary">Log Out</Button></p>
                {content}
                <HistogramAverageBuySell />
                <TableEndingPosition />
                <TableEffectiveReleasedProfit />
            </div>
        );
    }
}
