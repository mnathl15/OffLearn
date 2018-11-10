
import React, { Component } from 'react';
import { Button, Form, FormGroup, Input, Row, Col, Fade } from 'reactstrap';
import {Utils} from "../utils/utils"
import {Constants} from "../utils/constants"
import axios from 'axios';


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

    getHistory(){
      console.log(this.state.topics);
      
      axios.get(Constants.fileListUrl)
        .then(res => {
          this.setState({topics: res.data.data});
        })
    }

    render() {
        return (
          <div>
            <Button color="primary" onClick={this.toggle}>Toggle Fade</Button>
                <Fade in={this.state.fadeIn} tag="h5" className="mt-3">
                  Peek a Boo
                </Fade>
          </div>
        );
    }
}
