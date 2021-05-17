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

@bp.route('/create/', methods=['POST'])
def model_create():
    db = get_db()
    payload = request.get_json()
    name = payload.get('name')
    word_dimension = payload.get('word_dimension')
    batch_size = payload.get('batch_size')
    character_dimension = payload.get('character_dimension')
    dropout_rate = payload.get('dropout_rate')
    learning_rate = payload.get('learning_rate')
    context_len = payload.get('context_len')
    error = None

    if not name:
        error = "Model Name is required"
    elif db.execute(
        'SELECT id FROM model_info where name = ?', [name]
    ).fetchone() is not None:
        error = "Model name already exists."

    if error is not None:
        return make_response(error, 400)

    db.execute(
        'INSERT INTO model_info (name, word_dimension, batch_size, character_dimension, dropout_rate, learning_rate, context_len) '
        'VALUES(?, ?, ?, ?, ?, ?, ?);',
        [name, word_dimension, batch_size,character_dimension, dropout_rate, learning_rate, context_len]
    )

    db.commit()
    return make_response(jsonify({'message': 'success' }), 200)


