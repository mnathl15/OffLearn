import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import {Input, Row, ButtonDropdown, DropdownToggle, DropdownMenu, DropdownItem} from 'reactstrap';
import {SearchBar} from "./components/searchBar"
import { FileExplorer } from "./components/fileExplorer"
import { Label, Badge,Alert,Button,Fade } from 'reactstrap';
import { Constants } from './utils/constants';



class App extends Component {

  constructor(props) {
   super(props);

   this.toggle = this.toggle.bind(this);
   this.state = {
     dropdownOpen: false
   };
 }

 toggle() {
   this.setState({
     dropdownOpen: !this.state.dropdownOpen
   });
 }

  render() {
    return (
      <div className="App">
        <img height="92px" src=""/>
        <h1 className = "heading">{Constants.APP_NAME}</h1>
        <SearchBar/>
        <FileExplorer/>
      </div>
    );
  }


}

export default App;
