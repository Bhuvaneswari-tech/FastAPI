Scenario: Simple Library API
We want:
GET /books → List all books
Use a service layer
Use a repository layer
Inject service using Depends()
No database — just in-memory list.

Architecture
Client
   ↓
Controller (API Layer)
   ↓
Service (Business Logic)
   ↓
Repository (Data Layer)