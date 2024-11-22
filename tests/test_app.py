from http import HTTPStatus


def test_read_root_deve_retornar_OK_e_eu_gosto_de_pizza(client):
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Eu gosto de pizza'}
