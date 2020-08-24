import React from 'react';
import { Jumbotron, Container, Col, Button } from 'reactstrap';


const startPage = (props) => {
    return (
     <div>
      <Jumbotron fluid>
       <Container fluid>
        <h1 className="display-3"> Online Trading Platform </h1>
        <p className="lead">Build on Your Investments</p>
        <Button color="secondary" size="sm">Log in</Button>
        <Col>
         <img src="../../invest.png" alt='startImage' roundedCircle />
        </Col>
       </Container>      
      </Jumbotron>    
     </div>  
    );
};

export default startPage;