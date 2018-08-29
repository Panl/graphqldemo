import React, { Component } from 'react';
import './PoemEditor.css'
import { Mutation } from "react-apollo";
import { CREATE_POEM, UPDATE_POEM } from '../gql/Mutation';
import { QUERY_POEM_LIST } from '../gql/Query';

class PoemEditor extends Component {

    constructor(props) {
        super(props)
        this.state = {
            poemName:"",
            poemContent: "",
        }
    }

    nameChange = (event) => {
        this.setState({poemName: event.target.value})
    }

    contentChange = (event) => {
        this.setState({poemContent: event.target.value})
    }

    saveClick = () => {
        this.props.doMutate && this.props.doMutate({
            variables: {
                name: this.state.poemName,
                content: this.state.poemContent,
            }
        })
    }

    render = () => {
        return (
          <div className="poem-editor">
            <input className="edit-title" placeholder="标题" value={this.state.poemName} onChange={this.nameChange}/>
            <textarea className="edit-content" placeholder="内容" value={this.state.poemContent} onChange={this.contentChange}/>
            <button className="save-btn" onClick={this.saveClick}>保存</button>
          </div>
        )
    }
}

const _mutateUpdate = (cache, { data: { createPoem } }) => {
    let { poemList } = cache.readQuery({
        query: QUERY_POEM_LIST,
    })
    poemList = [createPoem.poem].concat(poemList);
    cache.writeQuery({
        query: QUERY_POEM_LIST,
        data: { poemList },
    })
}


export const PoemEditorMutation = ()=>{
   return(
        <Mutation mutation={CREATE_POEM} update={_mutateUpdate}>
            {(doMutate, {data })=>{
               return (<PoemEditor doMutate={doMutate}/>)
            }}
        </Mutation>
    )
}