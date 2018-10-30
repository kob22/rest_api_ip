
import pytest
from flask import jsonify, json
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_single_ip(client):

    rv = client.get('/?ip=8.8.8.8')
    json_data = rv.get_json()
    right_answer = {'North Countries': ['United States']}
    assert json_data == right_answer

def test_south_country(client):
    rv = client.get('/?ip=179.64.0.0')

    json_data = rv.get_json()
    right_answer = {'North Countries': []}
    assert json_data == right_answer

def testnocountry(client):
    rv = client.get('/')

    json_data = rv.get_json()
    right_answer = {'North Countries': []}
    assert json_data == right_answer

def testtoo_many(client):

    rv = client.get('/?ip=8.8.8.8&ip=138.8.8.8&ip=45.8.8.8&ip=10.8.8.8&ip=32.8.2.8&ip=22.8.77.8')

    json_data = rv.get_json()
    right_answer = {'North Countries': []}
    assert json_data == right_answer


def testnorthAndSouthCountry(client):
    rv = client.get('/?ip=8.8.8.8&?ip=179.64.0.0&ip=157.253.0.0&ip=2.92.0.0&ip=1.120.0.0')

    json_data = rv.get_json()
    right_answer = {'North Countries': ['Colombia', 'Russia', 'United States']}
    assert json_data == right_answer

def testwithletters(client):
    rv = client.get('/?ip=88.8.8&ip=179.64.0.0&ip=157.253.0.0&ip=2.92.0.0&ip=1.f.0.0')

    json_data = rv.get_json()
    right_answer = {'North Countries': ['Colombia', 'Russia']}
    assert json_data == right_answer
