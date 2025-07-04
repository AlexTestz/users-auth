# 🛡️ Validate Token Microservice (users-auth)

This microservice validates JWT tokens to ensure authenticated access to the resources of the **My Pet Host** system.

---

## 🚀 Technologies

- **Language:** Python 3.10
- **Framework:** FastAPI
- **Database:** PostgreSQL 
- **Authentication:** JWT (JSON Web Token) using PyJWT
- **Validation:** Pydantic
- **Docker:** For deployment and portability

---

## 📡 Architecture Style

- **API Type:** RESTful
- **Architectural Style:** Microservices
- **Communication:** HTTP
- **Exposed Endpoint:** `/api/auth/validate-token` (GET)

---

## 🏗️ Internal Architecture

- **Architecture Pattern:** Layered pattern (n-layer)
  - **Routes (API Router):** Defines the HTTP endpoints
  - **Controllers:** Token validation logic
  - **Schemas:** Data validation with Pydantic
  - **Utilities:** JWT handling and decoding

---

## 🧩 Applied Design Patterns

- **KISS:** Simple and direct code, easy to maintain.
- **DRY:** Reuse of common logic and utilities.
- **SOLID:** Separation of responsibilities in routes, controllers, and utilities.
- **YAGNI:** Only implement what is necessary for token validation.

---

## 🔐 Security

- **JWT:** The token is validated on each protected request, extracting the user_id and verifying its validity and expiration.
- **CORS:** Configurable with FastAPI Middleware (add as needed for frontend).

---

## 📦 Project Structure



```
validate-token/
├── src/
│   ├── main.py
│   ├── routes/
│   ├── controllers/
│   ├── schemas/
│   └── utils/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## ⚙️ Execution

**Modo local:**
```bash
python -m venv venv
source venv/bin/activate   # o .\venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn src.main:app --reload --port 3010
```

**Docker local:**
```bash
docker build -t validate-token .
docker run -p 3010:3010 --env-file .env validate-token
```

---

## 🛠️ Main endpoint

- `GET /api/auth/validate-token`

GET http://3.214.168.136:8000/api/users/validate-token

HEADERS Authorization           Bearer  TOKEN

**Headers requeridos:**
```
Authorization: Bearer <token>
```

**Respuesta Exitosa (200):**
```json
{
  "message": "✅ Token válido",
  "user_id": 7,
  "exp": 1719876543
}
```

| Código | Motivo                        |
| ------ | ----------------------------- |
| 401    | Invalid or expired token      |
| 422    | invalid format in token       |

**Swagger:**  
http://3.223.253.161:3008/docs

---

## 📚 Notes

- Decoupled architecture, each microservice is independent.
- The n-layer pattern facilitates maintenance and scalability.
- CORS can be configured according to the origin of your frontend.
- Complies with KISS, DRY, SOLID, and YAGNI principles for clean and maintainable code.

---