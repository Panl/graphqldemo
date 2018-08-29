import React, { Component } from 'react';
import logo from './logo.svg';
import PoemList from './components/PoemList';
import {PoemEditorMutation} from './components/PoemEditor';
import './App.css';
import { ApolloProvider } from 'react-apollo';
import client from "./conf/apollo";
import { QUERY_POEM } from './gql/Query';
import PoemDetail from './components/PoemDetail';


class App extends Component {

  render() {
    return (
      <ApolloProvider client={client}>
        <div className="App">
          <header className="App-header">
            <h1 className="App-title">Write Poem</h1>
          </header>
          <div className="App-body">
            <PoemList/>
            <PoemEditorMutation/>
          </div>
        </div>
      </ApolloProvider>
    );
  }
}

export default App;
