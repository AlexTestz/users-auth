# 🔐 Login User Microservice – users-auth

Allows users to authenticate by generating and validating JWT tokens for secure access to system resources.

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
- **Communication:** HTTP
- **Exposed Endpoints:**  
  - `/api/auth/login` (POST)  
  - `/api/auth/validate-token` (GET)

  POST http://3.214.168.136:8000/api/users/login 

  BODY
```json
{
  "username_or_email": "alexadmin@hotmail.com",
  "password": "EXAMPLE!"
}

GET http://3.214.168.136:8000/api/users/validate-token

HEADERS :  Authorization  Bearer  token

---

## 🏗️ Internal architecture

- **Architecture pattern:** Separation by layers (n-layers)
  - **Routes (API Router):** Defines HTTP endpoints
  - **Controllers:** Business logic
  - **Schemas:** Data validation with Pydantic
  - **Database:** Access and connection
  - **Utilities:** JWT handling
  - **Configuration:** Environment variables

---

## 🧩 Applied design patterns

- **KISS:** Simple and straightforward code, easy to maintain.
- **DRY:** Reuse of common logic and utilities.
- **SOLID:** Separation of responsibilities in routes, controllers, and utilities.
- **YAGNI:** Only what is necessary for login and token validation is implemented.

---
## 🔐 Security

- **JWT:** The token is generated and validated during each authentication, extracting the user_id from the payload.
- **CORS:** Allows requests from any origin (`allow_origins=[“*”]`), configurable for production.
- **Hashing:** Passwords stored and compared using bcrypt.

---

## 📦 Project structure

```
login-user/
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

**Modo local:**
```bash
uvicorn src.main:app --reload --port 3008
```

**Local Docker:**
```bash
docker build -t login-user .
docker run -p 3008:3008  login-user
```

---

## 🛠️ Main endpoints

- `POST /api/users/login`  
  Authenticates the user and returns a JWT.

- `GET /api/users/validate-token`  
  Validates the JWT sent in the Authorization header.



**Swagger:**  
http://3.223.253.161:3007/docs 
http://3.223.253.161:3008/docs 
---

## 📚 Notes

- Decoupled architecture, each microservice is independent.
- The n-layer pattern facilitates maintenance and scalability.
- JWT ensures that only authenticated users can access protected resources.
- CORS open for development, restrict in production.
- Complies with KISS, DRY, SOLID, and YAGNI principles for clean and maintainable code.
---