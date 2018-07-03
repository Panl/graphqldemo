import React, { Component } from 'react';
import './FolkEditor.css'
import { Mutation } from "react-apollo";
import { CREATE_POEM } from '../gql/Mutation';

class FolkEditor extends Component {

    constructor(props) {
        super(props)
        this.state = {
            folkName:"",
            folkContent: "",
        }
    }

    nameChange = (event) => {
        this.setState({folkName: event.target.value})
    }

    contentChange = (event) => {
        this.setState({folkContent: event.target.value})
    }

    saveClick = () => {
        this.props.doMutate && this.props.doMutate({
            variables: {
                name: this.state.folkName,
                content: this.state.folkContent,
            }
        })
    }

    render = () => {
        return (
          <div className="folk-editor">
            <input className="edit-title" placeholder="标题" value={this.state.folkName} onChange={this.nameChange}/>
            <textarea className="edit-content" placeholder="内容" value={this.state.folkContent} onChange={this.contentChange}/>
            <button className="save-btn" onClick={this.saveClick}>保存</button>
          </div>
        )
    }
}



export const FolkEditorMutation = ()=>{
   return(
        <Mutation mutation={CREATE_POEM}>
            {(doMutate, {data })=>{
                console.log('pl====', data)
               return (<FolkEditor doMutate={doMutate}/>)
            }}
        </Mutation>
    )
}