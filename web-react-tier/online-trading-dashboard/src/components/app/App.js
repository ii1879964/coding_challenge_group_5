import React, { Component } from 'react';
import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { Container } from 'reactstrap';
import Header from '../pages/Header'
import StartPage from '../pages/startPage';
import LoginPage from '../pages/LoginPage';
import HistogramAverageBuySell from '../pages/HistogramAverageBuySell'

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loggedInStatus: false,
      user: {}
    }
    this.handleLogin = this.handleLogin.bind(this);
  }
  
  handleLogin(user) {
    this.setState({
      loggedInStatus: true,
      user: user
    });
  }

  render() {
    const { loggedInStatus } = this.state;

    return (
      <div className="App">
        <Container>
          <Header/>
        </Container>
        <BrowserRouter>
          <Switch>
            <Container>
              <Route
                exact
                path={"/"}
                render={props =>(
                  <StartPage
                    {...props}
                    handleLogin={this.handleLogin}
                    loggedInStatus={loggedInStatus}
                  />
                )}
              />
              <Route
                exact
                path={"/dashboard"}
                render={props =>(
                  <HistogramAverageBuySell
                    {...props}
                    handleLogin={this.handleLogin}
                    loggedInStatus={loggedInStatus}
                  />
                )}
              />
              <Route
                exact
                path={"/login"}
                render={props =>(
                  <LoginPage
                    {...props}
                    handleLogin={this.handleLogin}
                    loggedInStatus={loggedInStatus}
                  />
                )}
              />
            </Container>
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}
