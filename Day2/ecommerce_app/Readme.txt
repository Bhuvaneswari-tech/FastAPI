Use Case: Product Management API
We are building a small system where:
Admin can create a product
Anyone can view products
We will implement only one entity: Product

Architecture Flow

Client (Swagger)
        ↓
Controller (API Layer)
        ↓
Service (Business Logic)
        ↓
Repository (Database Access)
        ↓
PostgreSQL

database.py

It is responsible for:
Creating DB connection
Creating session factory
Defining Base model
Providing DB dependency for APIs

create_engine
Creates the connection to PostgreSQL.
DATABASE_URL = settings.database_url

sessionmaker
Creates database sessions (used to talk to DB).

declarative_base
Used to define ORM models (tables).

settings
Comes from your configuration file:

Engine
This is your core connection interface
Manages connection pool
Talks to PostgreSQL

session
Temporary DB conversation
used to execute queries
Handles transactions

Base Class
All your models inherited here
It helps SQL alchemy
Map classes to database tables

DI
The fastAPI dependecy injection pattern it has to follow

API request comes
1. create DB session
2. pass it to API
3. Execute Logic
4. close session automatically

yield instead of return
yield allows cleanup after request finishes
finally ensures DB session closes
prevent connection leaks
