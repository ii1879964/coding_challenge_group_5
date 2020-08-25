import React, { PureComponent } from 'react';
import { Progress } from 'reactstrap';
import {
  BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';

export default class HistogramAverageBuySell extends PureComponent {
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/30763kr7/';

  render() {
    const { data } = this.props;
    const max = data ? Math.max(...data.map(item => item.prices.sell), ...data.map(item => item.prices.buy)) : 0;
    const table = data ? data.map((row, index) => {
      const {name, prices}= row;
      return <div key={name+index+"price"}>
              <div className="text-center">{name}</div>
              <Progress color="success" value={prices.buy} max={max}>{prices.buy}</Progress>
              <Progress color="info" value={prices.sell} max={max}>{prices.sell}</Progress>
            </div>
    }) : null;

    return (
    <>
      <h2>Average Buy And Sell Prices Per Instrument</h2>
      <div className="instruments-prices">
        {table}
      </div>

      {/*<BarChart
        width={1032}
        height={300}
        data={this.state.data}
        margin={{
          top: 5, right: 5, left: 0, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="buy" fill="#8884d8" />
        <Bar dataKey="sell" fill="#82ca9d" />
      </BarChart>*/}
      </>
    );
  }
}
