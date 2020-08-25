import React, { Component } from 'react';
import { Jumbotron, Container, Col, Button } from 'reactstrap';
import Logo from "./logo.png";


export default class StartPage extends Component {
    constructor(props) {
        super(props);
        this.handleClickLogIn = this.handleClickLogIn.bind(this);
    }
    handleClickLogIn(event) {
        event.preventDefault();
        this.props.history.push("/login");
    }
    render(){
    return (
     <div>
      <Jumbotron fluid>
       <Container fluid>
        <h1 className="display-3"> Online Trading Dashboard </h1>
        <p className="lead">Build on Your Investments</p>
        <p><Button onClick = {this.handleClickLogIn} color="primary">Log in</Button></p>
        <Col>
         <img width="630"
           height="350"
           src={Logo} 
           alt='Logo'/>
        </Col>
       </Container>      
      </Jumbotron>    
     </div>  
    );
};
};
