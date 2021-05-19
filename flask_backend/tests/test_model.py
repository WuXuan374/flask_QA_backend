import pytest
from flask import g, session
from flaskr.db import get_db
import json

def test_evaluation(client):
    # 存在的数据
    response = client.get('/model/evaluation/?model_name=BIDAF')
    assert response.status_code == 200
    jsonData = json.loads(response.data)
    assert jsonData[0]['epoch'] == 1

    response = client.get('/model/evaluation/?model_name=test')
    assert response.status_code == 404


def test_info(client):
    response = client.get('/model/info/?model_name=RNet')
    assert response.status_code == 200
    jsonData = json.loads(response.data)
    assert jsonData['word_dimension'] == 150

    response = client.get('model/info/?model_name=Fake')
    assert response.status_code == 404

def test_create(client, app):
    # 合法的 POST 请求
    response = client.post(
        '/model/create/',
        json = {
            'name': 'test_model',
            'word_dimension': 200,
            'batch_size': 80,
            'character_dimension': 10,
            'dropout_rate': 0.2,
            'learning_rate': 0.2,
            'context_len': 150
        }
    )

    assert response.status_code == 200
    # with app.app_context():
    #     db = get_db()
    #     count = db.execute(
    #         'SELECT COUNT(id) FROM model_info where name = test_model'
    #     )
    #     assert count == 1

    # 不合法的 POST 请求，缺乏必填项 name
    response = client.post(
        '/model/create/',
        json = {
            'word_dimension': 200,
            'batch_size': 80,
            'character_dimension': 10,
            'dropout_rate': 0.2,
            'learning_rate': 0.2,
            'context_len': 150
        }
    )

    assert response.status_code == 400
    assert b'Model Name is required' in response.data

    # 不合法的 POST 请求，name 已经存在
    response = client.post(
        '/model/create/',
        json = {
            'name': 'BiDAF',
            'word_dimension': 200,
            'batch_size': 80,
            'character_dimension': 10,
            'dropout_rate': 0.2,
            'learning_rate': 0.2,
            'context_len': 150
        }
    )

    assert response.status_code == 400
    assert b'Model name already exists.' in response.data
