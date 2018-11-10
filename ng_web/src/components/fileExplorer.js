
import React, { Component } from 'react';
import { Button, Form, FormGroup, Input, Row, Col, Fade } from 'reactstrap';
import {Utils} from "../utils/utils"
import {Constants} from "../utils/constants"


export class FileExplorer extends Component {

    constructor(props) {
      super(props);
      this.state = {
        fadeIn: true,
        topicList: [],
       };
      this.toggle = this.toggle.bind(this);
      this.getTopics();
    }

    getTopics(){
        var json_string = Utils.getRequest(Constants.fileListUrl);
        console.log("JSON_STRING");
        console.log(json_string);
        console.log("Entering parse");
      //  var data = JSON.parse(json_string);
        console.log("Ended parse");
        console.log("DATA");
      //  console.log(data);
    }

    toggle() {
      this.setState({
        fadeIn: !this.state.fadeIn
      });
    }

    render() {
      const topic_group_style={
       position:'absolute',
       top:window.innerHeight/2 + 100,
       right:window.innerWidth/2 -320,
       height:100,
       width:800,
       borderRadius:10,
       fontSize:'30px',
       textAlign:'center',
     };

     const topic_button={
       backgroundColor:'white',
       height:50,
       width:50,
       fontSize:'20px',
       color:'black',
       textAlign:'center',
     };

     const fade={
       color:'white'
     }

      return (
        <div style={topic_group_style}>
          <Button style={topic_button} color="primary" onClick={this.toggle}>f </Button>
              <Fade in={this.state.fadeIn} tag="h5" style={fade}>
                  Wikipedia
              </Fade>
        </div>
      );
    }
}
