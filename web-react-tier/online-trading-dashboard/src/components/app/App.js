import React, { Component } from 'react';
import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { Container } from 'reactstrap';
import StartPage from '../pages/startPage';
import LoginPage from '../pages/LoginPage';
import DashboardPage from '../pages/DashboardPage'

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loggedInStatus: false,
      user: {}
    }
    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
  }
  
  handleLogin(user) {
    this.setState({
      loggedInStatus: true,
      user: user
    });
  }

  handleLogout() {
    this.setState({
      loggedInStatus: false,
      user: {}
    });
  }

  render() {
    const { loggedInStatus } = this.state;

    return (
      <div className="App">
        <Container>
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
                  <>
                    <DashboardPage
                      {...props}
                      handleLogin={this.handleLogin}
                      handleLogout={this.handleLogout}
                      loggedInStatus={loggedInStatus}
                    />
                  </>
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
