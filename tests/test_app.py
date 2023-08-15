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


@pytest.mark.asyncio
async def test_update_user(client):
    client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {'username': 'bob', 'email': 'bob@example.com'}


@pytest.mark.asyncio
async def test_delete_user(client):
    client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}
