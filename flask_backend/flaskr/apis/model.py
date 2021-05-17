from flask import Blueprint, request, make_response, jsonify
from ..db import get_db
import json
from flask_restplus import fields, marshal

bp = Blueprint('model', __name__, url_prefix='/model')

info_fields = {
    'name': fields.String,
    'dataset': fields.String,
    'word_dimension': fields.Integer,
    'batch_size': fields.Integer,
    'character_dimension': fields.Integer,
    'dropout_rate': fields.Float,
    'learning_rate': fields.Float,
    'context_len': fields.Integer
}

evaluation_fields = {
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

    return json.dumps(marshal(results, evaluation_fields))

@bp.route('/info/', methods=['GET'])
def model_info():
    db = get_db()
    model_name = request.args.get("model_name")
    if not model_name:
        result = db.execute(
            "SELECT * FROM model_info"
        ).fetchall()
    else:
        result = db.execute(
            "SELECT * FROM model_info WHERE name LIKE :search", {"search": "%" + model_name + "%"}
        ).fetchone()

    if result is None:
        return make_response(jsonify({'error': 'Model info of {}  Not found'.format(model_name)}), 404)

    return json.dumps(marshal(result,info_fields))
