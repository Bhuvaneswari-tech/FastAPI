def get_admin_token(client):
    client.post("/auth/register", json={
        "username": "admin1",
        "email": "admin1@test.com",
        "password": "pass123",
        "role": "admin"
    })

    login = client.post(
        "/auth/login",
        data={
            "username": "admin1@test.com",
            "password": "pass123"
        }
    )

    return login.json()["access_token"]


def get_employer_token(client):
    client.post("/auth/register", json={
        "username": "employer1",
        "email": "employer1@test.com",
        "password": "pass123",
        "role": "employer"
    })

    login = client.post(
        "/auth/login",
        data={
            "username": "employer1@test.com",
            "password": "pass123"
        }
    )

    return login.json()["access_token"]


def create_company(client, admin_token):
    response = client.post(
        "/admin/companies",
        json={
            "name": "Tech Corp",
            "location": "Chennai"
        },
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200
    return response.json()["id"]


def test_employer_can_create_job(client):
    admin_token = get_admin_token(client)
    company_id = create_company(client, admin_token)

    employer_token = get_employer_token(client)

    response = client.post(
        "/employer/jobs",
        json={
            "title": "Backend Developer",
            "description": "FastAPI + MySQL",
            "salary": 60000,
            "company_id": company_id
        },
        headers={"Authorization": f"Bearer {employer_token}"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Backend Developer"