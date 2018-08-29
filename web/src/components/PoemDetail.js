import React, { Component } from 'react';
import {Query} from 'react-apollo';
import { QUERY_POEM } from '../gql/Query';

class PoemDetail extends Component {

    render = () => {
        return (
            <Query query={QUERY_POEM} variables={{id: 1}}>
                {({ loading, error, data }) => {
                    if (loading) return <div>Fetching</div>
                    if (error) return <div>Error</div>
            
                    const name = data.poem.name;
                    const content = data.poem.content;
            
                    return (
                    <div>
                        <h1>{name}</h1>
                        <p>{content}</p>
                    </div>
                    )
                }}
            </Query>
        )
    }
}

export default PoemDetail;