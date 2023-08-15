import pytest


@pytest.mark.asyncio
def test_root_user_get(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {'users': []}


@pytest.mark.asyncio
async def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
    }
