from flask import Blueprint, request, make_response, jsonify
from ..db import get_db

bp = Blueprint('model', __name__, url_prefix='/model')


@bp.route('/model/evaluation/', methods=['GET'])
def model_evaluation():
    db = get_db()
    model_name = request.args.get("model_name")
    results = db.execute(
        "SELECT * FROM model_evaluation WHERE name LIKE '?%'",(model_name,)
    ).fetchall()
    print(results)
    if results is None:
        return make_response(jsonify({'error': 'Model evaluation record Not found'}), 404)

    return jsonify({'results': results})
