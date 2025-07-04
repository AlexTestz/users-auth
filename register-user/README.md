# 📝 Register User Microservice (users-auth)

This microservice allows the registration of new users in the **My Pet Host** system. It is responsible for validating, encrypting, and storing users in the database.

---

## 🚀 Technologies

- **Language:** Python 3.10
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Hashing:** bcrypt for passwords
- **Validation:** Pydantic
- **Docker:** For deployment and portability

---

## 📡 Architecture Style

- **API Type:** RESTful
- **Architectural Style:** Microservices
- **Communication:** HTTP 
- **Exposed Endpoint:** `/api/users/register` (POST)

---

## 🏗️ Internal Architecture

- **Architecture Pattern:** Layered pattern (n-layer)
  - **Routes (API Router):** Defines the HTTP endpoints
  - **Controllers:** Business logic and validations
  - **Schemas:** Data validation with Pydantic
  - **Database:** Access and connection to PostgreSQL

---

## 🧩 Applied Design Patterns

- **KISS:** Simple and direct code, easy to maintain.
- **DRY:** Reuse of common logic and utilities.
- **SOLID:** Separation of responsibilities in routes, controllers, and utilities.
- **YAGNI:** Only implement what is necessary for user registration.

---

## 🔐 Security

- **Hashing:** Passwords stored and compared using bcrypt.
- **Validations:** Strong password (minimum 8 characters, uppercase, lowercase, number, and special character).
- **CORS:** Configurable with FastAPI Middleware (add as needed for frontend).

---

## 📦 Project Structure


```
register-user/
├── src/
│   ├── main.py
│   ├── routes/
│   ├── controllers/
│   ├── schemas/
│   └── database/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## ⚙️ Execution 

**Local mode :**
```bash
python -m venv venv
source venv/bin/activate   # o .\venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn src.main:app --reload --port 3006
```

**Local Docker:**
```bash
docker build -t register-user .
docker run -p 3006:3006 register-user
```

**DockerHub:**
```bash
docker pull alexmpz/register-user-service:qa
docker run -d -p 3006:3006 alexmpz/register-user-service:qa
```

---

## 🛠️ Main endpoint

- `POST /api/users/register`

POST http://3.214.168.136:8000/api/users/register

HEADERS     Content-Type      application/json

**Body example:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "MiContrasena123!",
  "role": "usuario"
}
```

**Validations performed:**
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (!@#$...)

**Succesfull response (201):**
```json
{
  "message": "✅ User registered successfully",
  "user": {
    "id": 7,
    "username": "johndoe",
    "email": "john@example.com",
    "role": "usuario"
  }
}
```

| Código | Motivo                                           |
| ------ | -----------------------------------------------  |
| 400    | Weak password                                    |
| 409    | User with that email or username already exists  |
| 422    | Invalid data format                              |
| 500    | Internal server error                            |

**Swagger:**  
http://3.223.253.161:3006/docs

---

## 📚 Notes

- Decoupled architecture, each microservice is independent.
- The n-layer pattern facilitates maintenance and scalability.
- CORS can be configured according to the origin of your frontend.
- Complies with KISS, DRY, SOLID, and YAGNI principles for clean and maintainable code.

---