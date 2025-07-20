from http import HTTPStatus


def test_read_root_deve_retornar_OK_e_ola_mundo(client):
    response = client.get('/')  # Act (ação do teste)
    assert response.status_code == HTTPStatus.OK  # Assert (verificação do teste)
    assert response.json() == {'message': 'Olá Mundo'}  # Assert (verificação do teste)


def test_create_user(client):
    response = client.post(
        '/users', json={'username': 'alice', 'email': 'alice@example.com', 'password': 'secret'}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'id': 1, 'email': 'alice@example.com', 'username': 'alice'}


def test_read_user(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'data': {'users': [{'id': 1, 'username': 'alice', 'email': 'alice@example.com'}]},
        'pagination': {'page': 1, 'size': 1, 'total': 1, 'total_pages': 1},
    }

def test_read_user_by_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'id': 1, 'username': 'alice', 'email': 'alice@example.com'}

def test_read_user_by_id_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário com ID 999 não encontrado.'}    

def test_update_user(client):
    response = client.put(
        '/users/1', json={'username': 'alice_updated', 'email': 'bob@example.com', 'password': 'newpassword'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'id': 1, 'username': 'alice_updated', 'email': 'bob@example.com', 'id': 1}

def test_update_user_not_found(client):
    response = client.put(
        '/users/999',
        json={'username': 'notfound', 'email': 'notfound@example.com', 'password': '123'}  
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário com ID 999 não encontrado.'}

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.NO_CONTENT

def test_delete_user_not_found(client):
    response = client.delete('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário com ID 999 não encontrado.'}   
