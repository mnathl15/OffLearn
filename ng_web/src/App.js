import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import { Button, Input, Row, ButtonDropdown, DropdownToggle, DropdownMenu, DropdownItem} from 'reactstrap';
import {SearchBar} from "./components/searchBar"
import { FileExplorer } from "./components/fileExplorer"
import { Label } from 'reactstrap';
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
<<<<<<< HEAD
        <header className="App-header">
          Offline Sites
        </header>
        <body className="App-body">
          <Input name="search" id="exampleEmail" placeholder="Search for a topic"/>
          <Button color="info">Search</Button>{' '}
        </body>
        <footer className="App-footer">
          <ButtonDropdown isOpen={this.state.dropdownOpen} toggle={this.toggle}>
            <DropdownToggle caret>
              Topic 1
            </DropdownToggle>
            <DropdownMenu>
              <DropdownItem>Wikipedia</DropdownItem>
              <DropdownItem>Encyclopedia</DropdownItem>
            </DropdownMenu>
          </ButtonDropdown>
        </footer>
=======
        <Label>{Constants.APP_NAME}</Label>
        <SearchBar/>
        <FileExplorer/>
>>>>>>> 78de365361ecb52cf9c85ace2629a0a2b5718cb8
      </div>
    );
  }
}

export default App;
