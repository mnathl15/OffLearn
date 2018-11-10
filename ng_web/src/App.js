import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Button } from 'reactstrap';
import {Utils} from "./utils/utils"
import {Constants} from "./utils/constants"

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
        <Button color="warning" onClick={() => {Utils.searchQuery("test")}}>danger</Button>
        </header>
      </div>
    );
  }
}

export default App;
