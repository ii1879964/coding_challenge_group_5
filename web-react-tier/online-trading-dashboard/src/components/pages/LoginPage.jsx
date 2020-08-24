import React, { Component } from 'react';
import { Form, FormGroup, Col, Input, Label, Button } from 'reactstrap';
//import AuthService from '../../services/authService';

export default class Login extends Component {
    //authService = new AuthService();

    constructor(props) {
        super(props);
        this.state = {
            LoginEmail: "",
            LoginPassword: "",
            LoginErrors: ""
        }

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }
    
    handleSubmit(event) {
        const {loginEmail, loginPassword} = this.state;
        //this.authService.login(loginEmail, loginPassword);
        this.props.handleLogin({
            user: {
                email: loginEmail,
                password: loginPassword
            }
        })
        event.preventDefault();
        this.props.history.push("/login");
    }

    handleChange(event) {
        console.log("handle change", event);
        this.setState({
            [event.target.name]: event.target.value
        });
    }
    
    render() {
        const { loggedInStatus } = this.props;

        const LoginForm = (
            <Form onSubmit={this.handleSubmit}>
                <FormGroup row>
                    <Label for="loginEmail" sm={1}>Email</Label>
                    <Col sm={3}>
                        <Input type="email" 
                            placeholder="Enter your email here" 
                            id="loginEmail"
                            value={this.state.email}
                            onChange={this.handleChange}
                            required       
                        />
                    </Col>
                </FormGroup>
                <FormGroup row>
                    <Label for="loginPassword" sm={1}>Password</Label>
                    <Col sm={3}>
                        <Input type="password"
                            placeholder="Enter your password here" 
                            id="loginPassword"
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
                {content}
            </div>
        );
    }
}