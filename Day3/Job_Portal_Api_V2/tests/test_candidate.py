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


def get_candidate_token(client):
    client.post("/auth/register", json={
        "username": "candidate1",
        "email": "candidate1@test.com",
        "password": "pass123",
        "role": "candidate"
    })

    login = client.post(
        "/auth/login",
        data={
            "username": "candidate1@test.com",
            "password": "pass123"
        }
    )

    return login.json()["access_token"]


def test_candidate_can_apply_job(client):
    # Step 1: Admin creates company
    admin_token = get_admin_token(client)
    company_id = create_company(client, admin_token)

    # Step 2: Employer login
    employer_token = get_employer_token(client)

    # Step 3: Employer creates job (VALID schema)
    create = client.post(
        "/employer/jobs",
        json={
            "title": "Fullstack Dev",
            "description": "React + FastAPI",
            "salary": 70000,
            "company_id": company_id
        },
        headers={"Authorization": f"Bearer {employer_token}"}
    )

    assert create.status_code == 200
    job_id = create.json()["id"]

    # Step 4: Candidate login
    candidate_token = get_candidate_token(client)

    # Step 5: Candidate applies
    apply = client.post(
        f"/candidate/apply/{job_id}",
        headers={"Authorization": f"Bearer {candidate_token}"}
    )

    assert apply.status_code == 200