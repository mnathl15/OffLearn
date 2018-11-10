import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {SearchBar} from "./components/searchBar"
import { FileExplorer } from "./components/fileExplorer"
import { Label, Badge,Alert,Button,Fade } from 'reactstrap';
import { Constants } from './utils/constants';



class App extends Component {
  render() {
    return (

      <div className="App">
    <Alert color="primary">
        Your offline gateway to knowledge!
      </Alert>

      <img height="92px" src=""/>

         <h1 className = "heading">{Constants.APP_NAME}</h1>
        <SearchBar/>
        <FileExplorer/>

      </div>
    );
  }


}

export default App;
