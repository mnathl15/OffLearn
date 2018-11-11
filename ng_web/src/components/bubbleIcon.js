
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

    renderPageList(){
        var pageList = []
        this.props.pages.forEach(page => {
            pageList.push(
                <Row>
                    <div className="col-md-12">
                        <Label><a style={{"color": "inherit"}} href={page}>{page}</a></Label>
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
                <Button style={topic_button} onClick={this.toggle}/>
                <Fade in={this.state.fadeIn} tag="h5" className="mt-3" style={{textAlign:'center',}}>
                    {this.renderPageList()}
                </Fade>
            </Col>
        );
    }


}
