Use Case: Simple Job Portal API

We are building a small system where:

Role	    What They Can Do
Candidate	    View jobs
Employer	    Post jobs
Admin	        Delete jobs

We will implement:

User Registration
User Login
JWT Token Generation
Role-Based Route Protection(RBAC)

Database
job_db

| Package         | Purpose                 |
| --------------- | ----------------------- |
| fastapi         | API framework           |
| uvicorn         | ASGI server             |
| sqlalchemy      | ORM                     |
| psycopg2-binary | PostgreSQL driver       |
| python-jose     | JWT creation/validation |
| passlib[bcrypt] | Password hashing        |
| python-dotenv   | Read .env file          |
| pydantic        | Data validation         |

#JWT - Token Format
#OAuth2 - Authorization framework for token-based authentication