#!/usr/bin/env python3
# coding: utf-8

from flask import Flask
from flask_graphql import GraphQLView
from folk.gql.schema import schema
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
