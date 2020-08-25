import React, {Component} from 'react';
import HistogramAverageBuySell from '../pages/HistogramAverageBuySell'
import AlertDB from '../pages/AlertDB'
import TableEndingPosition from '../pages/TableEndingPosition'
import TableEffectiveReleasedProfit from '../pages/TableEffectiveReleasedProfit'
import { Button } from 'reactstrap';
import "./DashboardPage.css";
import ConnectionService from '../../services/connectionService';
import TabelHistoricData from './TabelHistoricData';

export default class Dashboard extends Component {
    connectionService = new ConnectionService();

    constructor(props) {
        super(props);
        this.state = {
            IsConnectedDataBase: true
        }
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.handleLogout();
        this.props.history.push("/");
    }


    componentDidMount() {
        this.connectionService.getEndingPosition().then(response => {
            this.setState({
                position: response
            })
        });
        this.connectionService.getAveragePrice().then(response => {
            this.setState({
                prices: response
            });
        });
        this.connectionService.connectionCheck().then(response => {
            this.setState({
                IsConnectedDataBase: response === 200
            });
        });
        this.connectionService.getDealsHistory().then(response => {
            this.setState({
                historicData: response
            });
        });
        this.connectionService.getEffectiveBalance().then(response => {
            console.log(response);
        });
        this.connectionService.getRealizedBalance().then(response => {
            console.log(response);
        });
    }

    render(){
        const { IsConnectedDataBase } = this.state;

        const content = IsConnectedDataBase  ? null : <AlertDB/>;

        return (
            <div>
                <div className="header">
                    <h1>Online Trading Dashboard</h1>
                    <p><Button onClick = {this.handleSubmit} color="primary" className="logout-button">Log Out</Button></p>
                </div>
                {content}
                <HistogramAverageBuySell data={this.state.prices}/>
                <TableEndingPosition array={this.state.position}/>
                <TableEffectiveReleasedProfit />
                <TabelHistoricData data={this.state.historicData}/>
            </div>
        );
    }
}
