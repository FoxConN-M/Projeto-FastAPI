from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_OK_e_eu_gosto_de_pizza():
    client = TestClient(app)  # arrange
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Eu gosto de pizza'}
