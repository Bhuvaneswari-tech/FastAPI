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

Business Requirement
Build an E-Commerce backend that supports:
Product Management
Category Management
Order Management
Customer Management

Category ↔ Product Relationship
One Category can have Many Products
One Product belongs to One Category
This is called:
One-to-Many Relationship

Database Level
categories
    id (PK)

products
    id (PK)
    category_id (FK → categories.id)

Customer ↔ Order Relationship
This means:
One Customer can have Many Orders
One Order belongs to One Customer
This is called:
One-to-Many Relationship

Product ↔ Order Relationship
One Product can appear in Many Orders
One Order contains One Product
This is called:
One-to-Many Relationship

Complete Mapping Summary
Table	Relationship	Type
Category → Product	1 → Many	One-to-Many
Customer → Order	1 → Many	One-to-Many
Product → Order	    1 → Many	One-to-Many

Starlette
Its a lightweight ASGI framework for building async web services

FastAPI is built on top of Starlette

Routing
Middleware
REquest/REsponse handling
Exception handline

API simply extends Starlette with
Data Validation(pydantic)
Dependency injection
Automatic swagger docs
Type hint supports

Client Request
      ↓
Middleware (Before)
      ↓
Route Handler (Controller)
      ↓
Middleware (After)
      ↓
Response to Client

traceback
Used to print full stack trace when exception happens.