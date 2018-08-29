import gql from "graphql-tag"

export const QUERY_POEM = gql`
    query Poem($id: Int!) {
        poem(id: $id) {
            name
            content
        }
    }
`

export const QUERY_POEM_LIST = gql`
    query PoemList {
        poemList {
            id
            name
            content
        }
    }
`