import React, { Component } from 'react';
import logo from './logo.svg';
import FolkList from './components/FolkList';
import {FolkEditorMutation} from './components/FolkEditor';
import './App.css';
import { ApolloProvider } from 'react-apollo';
import client from "./conf/apollo";
class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <div className="App">
          <header className="App-header">
            <h1 className="App-title">Let's Folk</h1>
          </header>
          <div className="App-body">
            <FolkList/>
            <FolkEditorMutation/>
          </div>
        </div>
      </ApolloProvider>
    );
  }
}

export default App;
