
import React, { Component } from 'react';
import { Button, Form, FormGroup, Input, Row, Col, Fade } from 'reactstrap';
import {Utils} from "../utils/utils"
import {Constants} from "../utils/constants"
import axios from 'axios';
import {BubbleIcon} from './bubbleIcon'


export class FileExplorer extends Component {

    constructor(props) {
      super(props);
      this.state = { 
        fadeIn: true,
        topics: []
       };
      this.getHistory = this.getHistory.bind(this);
      setInterval(this.getHistory, 5000)

    }



    getHistory(){      
      axios.get(Constants.fileListUrl)
        .then(res => {
          this.setState({topics: res.data.data});
        })
    }

    render() {
      const topic_group_style={
       position:'absolute',
       top:window.innerHeight/2 + 100,
       height:100,
       width:"100%",
       borderRadius:10,
       fontSize:'30px',
       textAlign:'center',
     };

      return (
        <div style={topic_group_style}>
          <BubbleIcon name={"Poop"} pages={["uno", "dos", "tres"]}/>
        </div>
      );
    }
}
