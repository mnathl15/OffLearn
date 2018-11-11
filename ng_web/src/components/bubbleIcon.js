
import React, { Component } from 'react';
import { Button, Label, Fade, Col, Row } from 'reactstrap';

export class BubbleIcon extends Component {

    constructor(props){
        super(props);
        this.state={
            fadeIn: false
        }
        this.toggle = this.toggle.bind(this);
        
    }

    getSource(fileDir){
        var start = fileDir.lastIndexOf("\\")+1
        var end = fileDir.lastIndexOf(".")
        return fileDir.substring(start,end)
    }

    renderPageList(){
        var pageList = []
        this.props.pages.forEach(page => {
            pageList.push(
                <Row>
                    <div className="col-md-12">
                        <Label><a target="_blank" rel="noopener noreferrer" 
                            style={{"color": "inherit"}} href={page}>{this.getSource(page)}</a></Label>
                    </div>
                </Row>)
        });
        return pageList;
    }

    toggle() {
        this.setState({
            fadeIn: !this.state.fadeIn
        });
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
            <Col>
                <Button style={topic_button} onClick={this.toggle}>{this.props.name.substring(0,1)}</Button>
                <Fade in={this.state.fadeIn} tag="h5" className="mt-3" style={{textAlign:'center',}}>
                    {this.props.name}
                    {this.renderPageList()}
                </Fade>
            </Col>
        );
    }


}
