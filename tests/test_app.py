from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root_deve_retornar_OK_e_eu_gosto_de_pizza(client):
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Eu gosto de pizza'}


def test_create_user(client):
    response = client.post(  # User Schema
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    # Voltou correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar Userpublic
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'username2',
            'email': 'test@test.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'username2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
