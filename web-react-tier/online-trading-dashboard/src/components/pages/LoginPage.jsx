import React, { Component } from 'react';
import { Form, FormGroup, Col, Input, Label, Button, Alert } from 'reactstrap';
import ConnectionService from '../../services/connectionService';
 
export default class Login extends Component {
    connectionService = new ConnectionService();
 
    constructor(props) {
        super(props);
        this.state = {
            UserLogin: "",
            UserPassword: "",
            LoginErrors: ""
        }
 
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleSubmit(event) {
        const {UserLogin, UserPassword} = this.state;
        this.connectionService.loginCheck(UserLogin, UserPassword).then(status => {
            if(status === 200) {
                
                this.props.handleLogin({
                    user: {
                        login: UserLogin,
                        password: UserPassword
                    }
                });
                this.setState({
                    LoginErrors: ""
                });
                this.props.history.push("/dashboard");
    
            } else {
                this.setState({
                    LoginErrors: "Wrong login/password"
                });
            }
        });
        event.preventDefault();
    }
 
    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }
    
    render() {
        const { loggedInStatus } = this.props;
        const { LoginErrors } = this.state;
 
        const errorContent = LoginErrors ? <Alert color="danger">{LoginErrors}</Alert> : null;
 
        const LoginForm = (
            <Form onSubmit={this.handleSubmit}>
                <FormGroup row>
                    <Label for="UserLogin" sm={1}>login</Label>
                    <Col sm={3}>
                        <Input type="text" 
                            placeholder="Enter your login here" 
                            id="UserLogin"
                            name="UserLogin"
                            value={this.state.login}
                            onChange={this.handleChange}
                            required       
                        />
                    </Col>
                </FormGroup>
                <FormGroup row>
                    <Label for="UserPassword" sm={1}>Password</Label>
                    <Col sm={3}>
                        <Input type="password"
                            placeholder="Enter your password here" 
                            id="UserPassword"
                            name="UserPassword"
                            value={this.state.password}
                            onChange={this.handleChange}
                            required       
                        />
                    </Col>
                </FormGroup>
                <Button type="submit" color="primary">Log in</Button>
            </Form>
        );
 
        const content = loggedInStatus ? <h2>Your are logged in</h2> : LoginForm;
 
        return (
            <div>
                {errorContent}
                {content}
            </div>
        );
    }
}