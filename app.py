from flask import Flask, jsonify, request
from ariadne import QueryType, make_executable_schema, graphql_sync

type_defs = """
scalar JSON

type Query {
    getClassByNameJSON(name: String!): JSON
}
"""

query = QueryType()

@query.field("getClassByNameJSON")
def resolve_get_class_by_name_json(*_, name):
    if name == "SAR":
        return {
            "name": "SAR",
            "ownedAttribute": [
                {
                    "aggregation": "composite",
                    "association": "_a1b2c3d4e5f6",
                    "name": "theta",
                    "type": [
                        {
                            "string_type": "_n1m2l3k4j5h6"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_u1v2w3x4y5z6",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_b2c3d4e5f6g7",
                    "name": "iota",
                    "type": [
                        {
                            "string_type": "_m2l3k4j5h6g7"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_v2w3x4y5z6a7",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_c3d4e5f6g7h8",
                    "name": "kappa",
                    "type": [
                        {
                            "string_type": "_l3k4j5h6g7f8"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_w3x4y5z6a7b8",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_d4e5f6g7h8i9",
                    "name": "lambda",
                    "type": [
                        {
                            "string_type": "_k4j5h6g7f8e9"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_x4y5z6a7b8c9",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_e5f6g7h8i9j0",
                    "name": "mu",
                    "type": [
                        {
                            "string_type": "_j5h6g7f8e9d0"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_y5z6a7b8c9d0",
                    "xmi_type": "Property"
                },
                {
                    "aggregation": "composite",
                    "association": "_f6g7h8i9j0k1",
                    "name": "nu",
                    "type": [
                        {
                            "string_type": "_h6g7f8e9d0c1"
                        }
                    ],
                    "visibility": "private",
                    "xmi_id": "_z6a7b8c9d0e1",
                    "xmi_type": "Property"
                }
            ],
            "xmi_id": "_20_0alpha_1234567_1234567890_123456_78901",
            "xmi_type": "Class"
        }

    return None

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
