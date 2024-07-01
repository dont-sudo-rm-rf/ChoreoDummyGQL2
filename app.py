from flask import Flask, jsonify, request
from ariadne import QueryType, make_executable_schema, graphql_sync
import json

type_defs = """
scalar JSON

type Query {
    getClassByNameJSON(name: String!): JSON
}
"""
with open("./output.json", 'r') as f:
    data = json.load(f)

query = QueryType()

@query.field("getClassByNameJSON")
def resolve_get_class_by_name_json(*_, name):
    return data

schema = make_executable_schema(type_defs, query)

app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run()
