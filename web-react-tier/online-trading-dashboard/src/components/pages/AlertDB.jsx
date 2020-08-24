import React from 'react';
import { Alert } from 'reactstrap';

const AlertDB = (props) => {
    return (
        <div>
            <Alert color="danger">
                Database is not connected.
            </Alert>
        </div>
    )
}

export default AlertDB;