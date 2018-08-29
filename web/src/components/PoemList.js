import React, { Component } from 'react';
import './PoemList.css'
import { QUERY_POEM_LIST } from '../gql/Query';
import { Query } from 'react-apollo';

class PoemList extends Component {

    

    render = () => {
        return (
            <div className="list-bar">
                <Query query={QUERY_POEM_LIST}>
                    {({loading, error, data})=>{
                        if (loading) return <div>Fetching</div>
                        if (error) return <div>Error</div>
                        console.warn('----',data);
                        var poemList = data.poemList;
                        return poemList.map((poem)=>{
                            return (
                                <div>
                                    <h3>{poem.name}</h3>
                                    <div>{poem.content}</div>
                                </div>
                            )
                        })
                    }}
                </Query>
            </div>
        )
    }
}

export default PoemList