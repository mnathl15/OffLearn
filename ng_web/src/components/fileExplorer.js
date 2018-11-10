
import React, { Component } from 'react';
import { Button, Form, FormGroup, Input, Row, Col, Fade } from 'reactstrap';
import {Utils} from "../utils/utils"
import {Constants} from "../utils/constants"


export class FileExplorer extends Component {
    constructor(props) {
      super(props);
      this.state = { fadeIn: true };
      this.toggle = this.toggle.bind(this);
    }

    toggle() {
      this.setState({
        fadeIn: !this.state.fadeIn
      });
    }

    render() {
        return (
          <div>
            <Button color="primary" onClick={this.toggle}>Toggle Fade</Button>
                <Fade in={this.state.fadeIn} tag="h5" className="mt-3">
                    This content will fade in and out as the button is pressed
                </Fade>
          </div>
        );
    }
}
