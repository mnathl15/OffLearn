import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {SearchBar} from "./components/searchBar"
import { FileExplorer } from "./components/fileExplorer"
import { Label } from 'reactstrap';
import { Constants } from './utils/constants';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Label>{Constants.APP_NAME}</Label>
        <SearchBar/>
        <FileExplorer/>
      </div>
    );
  }
}

export default App;
