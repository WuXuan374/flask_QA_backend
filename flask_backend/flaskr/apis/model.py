from flask import Blueprint, request, make_response, jsonify
from ..db import get_db
import json
from flask_restplus import fields, marshal

bp = Blueprint('model', __name__, url_prefix='/model')
resource_fields = {
    'name': fields.String,
    'epoch': fields.Integer,
    'exactMatch': fields.Float,
    'f1': fields.Float,
    'loss': fields.Float
}



@bp.route('/evaluation/', methods=['GET'])
def model_evaluation():
    db = get_db()
    model_name = request.args.get("model_name")
    results = db.execute(
        "SELECT * FROM model_evaluation WHERE name LIKE :search",{"search": model_name + "%"}
    ).fetchall()
    if results is None:
        return make_response(jsonify({'error': 'Model evaluation record Not found'}), 404)

    return json.dumps(marshal(results, resource_fields))
