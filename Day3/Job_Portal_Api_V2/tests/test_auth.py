def test_register_user(client):
    response = client.post("/auth/register", json={
        "username": "john",
        "email": "john@test.com",
        "password": "1234",
        "role": "candidate"
    })
    assert response.status_code == 200


def test_login_success(client):
    client.post("/auth/register", json={
        "username": "mark",
        "email": "mark@test.com",
        "password": "1234",
        "role": "candidate"
    })

    response = client.post(
        "/auth/login",
        data={"username": "mark@test.com", "password": "1234"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()

    response = client.post(
        "/auth/login",
        data={"username": "mark@test.com", "password": "1234"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()