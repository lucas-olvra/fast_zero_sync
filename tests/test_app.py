from http import HTTPStatus

from fast_zero.app import app
from fastapi.testclient import TestClient

client = TestClient(app)  # Arrange (organização do teste)


def test_read_root_deve_retornar_OK_e_ola_mundo():
    response = client.get('/')  # Act (ação do teste)
    assert response.status_code == HTTPStatus.OK  # Assert (verificação do teste)
    assert response.json() == {'message': 'Olá Mundo'}  # Assert (verificação do teste)
