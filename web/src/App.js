import React, { Component } from 'react';
import logo from './logo.svg';
import FolkList from './components/FolkList';
import FolkEditor from './components/FolkEditor';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Let's Folk</h1>
        </header>
        <div className="App-body">
          <FolkList/>
          <FolkEditor/>
        </div>
      </div>
    );
  }
}

export default App;
