import gql from "graphql-tag"

export const CREATE_POEM = gql`
    mutation CreatePoem($name: String!, $content: String!) {
        createPoem(name: $name, content: $content) {
            poem {
                id
                name
                content
            }
        }
    }
`

export const UPDATE_POEM = gql`
    mutation UpdatePoem($id: Int!, $name: String!, $content: String!) {
        updatePoem(id: $id, name: $name, content: $content) {
            poem {
                id
                name
                content
            }
        }
    }
`