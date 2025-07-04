# 🔑 Change Password Microservice – users-auth

Allows authenticated users to change their password by validating the JWT token and updating the database.

---

## 🚀 Technologies

- **Language:** Python 3.10
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Token) using PyJWT
- **Hashing:** bcrypt for passwords
- **HTTP Client:** httpx (for communication with other microservices)
- **CORS:** Configured with FastAPI Middleware

---

## 📡 Architecture Style

- **API Type:** RESTful
- **Architectural Style:** Microservices
- **Communication:** HTTP (no WebSocket, gRPC, SOAP, or GraphQL)
- **Exposed Endpoints:** `/api/users/change-password` (PUT)

PUT http://3.214.168.136:8000/api/users/change-password  
HEADERS  Authorization          Bearer TOKEN  
BODY  
```json
{
  "old_password": "admin123!",
  "new_password": "Admin123!"
}

---

## 🏗️ Arquitectura interna

- **Architecture pattern:** Separation by layers (n-layers)
  - **Routes (API Router):** Defines HTTP endpoints 
  - **Controllers:** Business logic 
  - **Schemas:** Data validation with Pydantic 
  - **Database:** Access and connection 
  - **Utilities:** JWT handling 
  - **Configuration:** Environment variables

---

## 🧩 Design patterns applied

- **KISS:** Simple and straightforward code that is easy to maintain.
- **DRY:** Reuse of common logic and utilities.
- **SOLID:** Separation of responsibilities in routes, controllers, and utilities.
- **YAGNI:** Only what is necessary for password change and validation is implemented.

---

## 🔐 Security

- **JWT:** The token is validated on each protected request, extracting the user_id from the payload.
- **CORS:** Allows requests from any origin (`allow_origins=[“*”]`), configurable for production.
- **Hashing:** Passwords stored and compared using bcrypt.
---

## 📦 Project structure

```
change-password/
├── src/
│   ├── main.py
│   ├── routes/
│   ├── controllers/
│   ├── schemas/
│   ├── database/
│   ├── utils/
│   └── config/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## ⚙️ Execution

**local mode:**
```bash
uvicorn src.main:app --reload --port 3009
```

**Local Docker:**
```bash
docker build -t change-password .
docker run -p 3009:3009 change-password
```

**DockerHub:**
```bash
docker pull alexmpz/change-password-service:qa
docker run -d -p 3009:3009  alexmpz/change-password-service:qa
```

---

## 🛠️ Main endpoint

- `PUT /api/users/change-password`

**Body example:**
```json
{
  "old_password": "MiContrasena123!",
  "new_password": "NuevaContrasena456!"
}
```

**Swagger:**  
http://3.223.253.161:3009/docs 

---

## ☁️ Upload to DockerHub

```bash
docker build -t alexmpz/change-password-service:qa .
docker push alexmpz/change-password-service:qa
```

---

## 📚 Notes

- Decoupled architecture, each microservice is independent.
- The n-layer pattern facilitates maintenance and scalability.
- JWT ensures that only authenticated users can change their password.
- CORS open for development, restrict in production.
- Complies with KISS, DRY, SOLID, and YAGNI principles for clean code and