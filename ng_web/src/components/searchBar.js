
import React, { Component } from 'react';
import { Button, Form, FormGroup, Input, Row, Col } from 'reactstrap';
import {Utils} from "../utils/utils"
import {Constants} from "../utils/constants"

export class SearchBar extends Component {
    constructor(props){
        super(props);
        this.state = {
            inputValue: ''
        }; this.updateInputValue = this.updateInputValue.bind(this)
    }
    updateInputValue(evt){
        this.setState({
            inputValue: evt.target.value
        });
    }
    render() {
        return (
          <Row>
            <Col md={{ size: 6, offset: 3 }}>
                <Row>
                    <Col xs="9">
                        <Input value={this.state.inputValue} onChange={evt => this.updateInputValue(evt)} placeholder="Search" />
                    </Col>
                    <Col xs="3">
                           <Button onClick={() =>{Utils.searchQuery(this.state.inputValue)}}>Search</Button>
                    </Col>
                </Row>
            </Col>
        </Row>
        );
    }
}