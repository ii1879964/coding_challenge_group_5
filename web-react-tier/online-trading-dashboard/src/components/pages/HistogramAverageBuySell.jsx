import React, { PureComponent } from 'react';
import {
  BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';

const data = [
  {
    name: 'Astronomica', buy: 4000, sell: 2400, amt: 2400,
  },
  {
    name: 'Borealis', buy: 3000, sell: 1398, amt: 5,
  },
  {
    name: 'Celestial', buy: 2000, sell: 9800, amt: 2290,
  },
  {
    name: 'Deuteronic', buy: 2780, sell: 3908, amt: 2000,
  },
  {
    name: 'Eclipse', buy: 1890, sell: 4800, amt: 2181,
  },
  {
    name: 'Floral', buy: 2390, sell: 3800, amt: 2500,
  },
  {
    name: 'Galactia', buy: 3490, sell: 4300, amt: 2100,
  },
  {
    name: 'Heliosphere', buy: 3490, sell: 4300, amt: 2100,
  },
  {
    name: 'Interstella', buy: 3490, sell: 4300, amt: 2100,
  },
  {
    name: 'Jupiter', buy: 3490, sell: 4300, amt: 2100,
  },
  {
    name: 'Koronis', buy: 3490, sell: 4300, amt: 2100,
  },
  {
    name: 'Lunatic', buy: 3490, sell: 4300, amt: 2100,
  },
];

export default class Example extends PureComponent {
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/30763kr7/';

  render() {
    return (
    <>
    <h2>Average Buy And Sell Prices Per Instrument</h2>
      <BarChart
        width={1032}
        height={300}
        data={data}
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
      </BarChart>
      </>
    );
  }
}
