import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Button, Input, Row, ButtonDropdown, DropdownToggle, DropdownMenu, DropdownItem} from 'reactstrap';

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
      </div>
    );
  }
}

export default App;
