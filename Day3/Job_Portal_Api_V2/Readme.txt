CASE STUDY: Enterprise Hiring Platform API
Business Problem
A company wants to build a backend system for a Hiring Platform with:
Users
Admin
Employer
Candidate
Companies
Managed by Admin
Employers belong to companies
Jobs
Employers post jobs
Candidates apply
Applications
Candidates apply
Employers view applications
Admin can manage all

BUSINESS RULES


job_portal/
│
├── .env
├── requirements.txt
│
├── app/
│   ├── main.py
│
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── pagination.py
│
│   ├── database/
│   │   ├── base.py
│   │   └── session.py
│
│   ├── models/
│   │   ├── user.py
│   │   ├── company.py
│   │   ├── job.py
│   │   └── application.py
│
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── company_schema.py
│   │   ├── job_schema.py
│   │   └── application_schema.py
│
│   ├── repositories/
│   │   ├── user_repo.py
│   │   ├── company_repo.py
│   │   ├── job_repo.py
│   │   └── application_repo.py
│
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── company_service.py
│   │   ├── job_service.py
│   │   └── application_service.py
│
│   ├── controllers/        ✅ NEW LAYER
│   │   ├── auth_controller.py
│   │   ├── admin_controller.py
│   │   ├── employer_controller.py
│   │   └── candidate_controller.py
│
│   ├── dependencies/
│   │   └── rbac.py
│
│   ├── middleware/
│   │   ├── logging.py
│   │   └── exception_handler.py
│
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── admin_router.py
│   │   ├── employer_router.py
│   │   └── candidate_router.py
│
└── tests/
    ├── test_auth.py
    ├── test_jobs.py

Request Flow Now
HTTP Request
   ↓
Router (defines endpoint)
   ↓
Controller (handles request/response mapping)
   ↓
Service (business logic)
   ↓
Repository (DB queries)
   ↓
Database

DATABASE RELATIONSHIPS
Company 1 ---- * Employer(User) , Employees
One Company - Many Employer
Company 1 ---- * Jobs
One Company Many Jobs
Job 1 ---- * Applications
One Job Many Applications
Candidate(User) 1 ---- * Applications
One Candidate Many Applications