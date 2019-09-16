from typing import Tuple, List
from flask import jsonify, g
from flask.wrappers import Response


def create_response(
    data: dict = {}, status: int = 200, message: str = ""
) -> Tuple[Response, int]:

    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary")
    
    data["message"] = message
    response = {"success": 200 <= status < 300, "result": data}
    return jsonify(response), status


def serialize_list(items: List, source: str, fields: List) -> List:
    if not items or items is None:
        return []

    new_list = list()
    for item in items:
        newdict = {k: item.k for k in fields}
        newdict['source'] = source
        new_list.append(newdict)

    return new_list

def all_exception_handler(error: Exception) -> Tuple[Response, int]:
    return create_response(message=str(error), status=500)
