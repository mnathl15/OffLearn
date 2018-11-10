
import React, { Component } from 'react';
import { Button, Form, FormGroup, Input, Row, Col } from 'reactstrap';
import {Utils} from "../utils/utils"
import {Constants} from "../utils/constants"

export class SearchBar extends Component {

    render() {
        return (
          <Row>
            <Col md={{ size: 6, offset: 3 }}>
                <Row>
                    <Col xs="9">
                        <Input placeholder="Search" />
                    </Col>
                    <Col xs="3">
                        <Button  onClick={() => {Utils.searchQuery("test")}}>Search</Button>
                    </Col>
                </Row>
            </Col>
        </Row>
        );
    }
}