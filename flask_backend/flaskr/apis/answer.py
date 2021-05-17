from flask import Blueprint, request, make_response, jsonify
from ..db import get_db
import json
from flask_restplus import fields, marshal

bp = Blueprint('answer', __name__, url_prefix='/answer')

fav_answer_fields = {
    'id': fields.Integer,
    'question': fields.String,
    'document_title': fields.String,
    'score': fields.Float,
    'answer': fields.String,
    'concrete_answer': fields.String
}

@bp.route('/subscribe', methods=['POST'])
def subscribe_answer():
    db = get_db()
    payload = request.get_json()
    question = payload.get('question')
    document_title = payload.get('document_title')
    score = payload.get('score')
    answer = payload.get('answer')
    concrete_answer = payload.get('concrete_answer')

    if not question or not document_title or not answer:
        make_response('question, document_title 和 answer 为必填项', 400)

    db.execute(
        'INSERT INTO fav_answer (question, document_title, score, answer, concrete_answer) '
        'VALUES(?, ?, ?, ?, ?);',
        [question, document_title, score, answer, concrete_answer]
    )

    db.commit()
    return make_response(jsonify({'message': '订阅成功!' }), 200)

@bp.route('/unSubscribe/<id>', methods=['DELETE'])
def unSubscribe_answer(id):
    db = get_db()

    db.execute(
        "DELETE FROM fav_answer WHERE id = ?", [id]
    )

    db.commit()
    return make_response(jsonify({'message': '取消订阅成功!' }), 200)




@bp.route('/favList', methods=['GET'])
def get_fav_answers():
    db = get_db()
    results = db.execute(
        'SELECT * FROM fav_answer'
    ).fetchall()
    if results is None:
        return make_response(jsonify({'error': 'empty list'}), 404)

    return json.dumps(marshal(results, fav_answer_fields))
