
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



      function changeButtonColor(){

        var button = document.getElementById('submit_button');

      }

      function onHover(){
        var button = document.getElementById('submit_button');
        button.style.backgroundColor = '#4A6572'

      }

      function onLeaveHover(){
        var button = document.getElementById('submit_button');
        button.style.backgroundColor = '#344955'

      }


      const search_styles={
        position:'absolute',
        top:window.innerHeight/2-50,
        right:window.innerWidth/2 -320,
        height:50,
        width:700,
        borderRadius:10,
        fontSize:'30px',
        textAlign:'center'


      };

      const button_styles={
        position:'absolute',
        top:window.innerHeight/2-50,
        right:window.innerWidth/2 -430,
        width:100,
        height:50,
        borderRadius:10,
        backgroundColor:'#344955',
        color:'white',
        fontSize: '20px',







      }



        return (

          <form>
            <label>
            <input value={this.state.inputValue}  onChange={evt => this.updateInputValue(evt)} style={search_styles} id = 'search' 
              placeholder="What are you looking for?" type="text" name= "name"/>
            <input style={button_styles} id = 'submit_button' type="button" value="Search"  onClick={() =>{Utils.searchQuery(this.state.inputValue)}},
                ()=>changeButtonColor() onMouseOver={()=>onHover()} onMouseLeave = {()=>onLeaveHover()}/>
            </label>

          </form>

        );
    }
}
