import React, { Component } from 'react';
import './FolkEditor.css'

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

export default FolkEditor