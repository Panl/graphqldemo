import gql from "graphql-tag"

export const CREATE_POEM = gql`
    mutation CreatePoem($name: String!, $content: String!) {
        createPoem(name: $name, content: $content) {
            poem {
                name
                content
            }
        }
    }
`