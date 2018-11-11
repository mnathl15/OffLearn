
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
      this.toggle = this.toggle.bind(this);
      this.getHistory = this.getHistory.bind(this);
      setInterval(this.getHistory, 5000)

    }

    toggle() {
      this.setState({
        fadeIn: !this.state.fadeIn
      });
    }


    renderBubbleIcons(){

      var topicList = []
      this.state.topics.forEach(topic => {

          topicList.push(
             <BubbleIcon name={topic.name} pages={topic.pages}/> 
          )
      });
      return topicList;


    }

    getHistory(){
      console.log(this.state.topics);

      axios.get(Constants.fileListUrl)
        .then(res => {
          this.setState({topics: res.data.data});
        })
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




        <Row style={topic_group_style}>
          {this.renderBubbleIcons()}
        </Row>




      );
    }
}
