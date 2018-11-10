
import React, { Component } from 'react';
import { Button, Form, FormGroup, Input, Row, Col, Fade } from 'reactstrap';

export class BubbleIcon extends Component {

    constructor(props){
        super(props);
    }

    render(){

        const topic_button={
            backgroundColor:'white',
            height:50,
            width:50,
            fontSize:'20px',
            color:'black',
            textAlign:'center',
            borderRadius: '30px'
        };
        return(
            <Button style={topic_button}>
                {this.props.name}
            </Button>
        );
    }


}