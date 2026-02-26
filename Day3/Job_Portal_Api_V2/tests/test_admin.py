def get_admin_token(client):
    # Register Admin
    client.post("/auth/register", json={
        "username": "admin2",
        "email": "admin2@test.com",
        "password": "pass123",
        "role": "admin"
    })

    # Login (OAuth2 requires form-data, not JSON)
    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin2@test.com",  # email inside username field
            "password": "pass123"
        }
    )

    return login_response.json()["access_token"]


def test_admin_can_create_company(client):
    admin_token = get_admin_token(client)

    response = client.post(
        "/admin/companies",
        json={
            "name": "Tech Corp",
            "location": "Chennai"
        },
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200


def test_admin_can_view_companies(client):
    admin_token = get_admin_token(client)

    response = client.get(
        "/admin/companies",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200


def test_admin_can_view_jobs(client):
    admin_token = get_admin_token(client)

    response = client.get(
        "/admin/jobs",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200


def test_admin_can_view_applications(client):
    admin_token = get_admin_token(client)

    response = client.get(
        "/admin/applications",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200