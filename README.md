# 👤 Users-Auth Domain – My Pet Host

The **users-auth** domain manages authentication, authorization, and user management within the **My Pet Host** ecosystem. It consists of independent microservices, each with a clear and well-defined responsibility.

---

## 🧩 Included Microservices

- **register-user:** Registration and validation of new users.
- **login-user:** Authentication and generation of JWT tokens.
- **change-password:** Secure password change for authenticated users.
- **validate-token:** Validation and decoding of JWT tokens.

---

## 🚀 Main Technologies

- **Language:** Python 3.10
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Token) using PyJWT
- **Hashing:** bcrypt for passwords
- **Validation:** Pydantic
- **HTTP Client:** httpx (for internal communication)
- **Docker:** For deployment and portability
- **CORS:** Configurable with FastAPI Middleware

---

## 📡 Architecture Style

- **API Type:** RESTful
- **Architectural Style:** Microservices
- **Communication:** HTTP 
- **Responsibility Separation:** Each microservice is autonomous and decoupled.

---

## 🏗️ Internal Architecture

- **Architecture Pattern:** Layered pattern (n-layer)
  - **Routes (API Router):** Defines the HTTP endpoints
  - **Controllers:** Business logic and validations
  - **Schemas:** Data validation with Pydantic
  - **Database:** Access and connection to PostgreSQL
  - **Utilities:** JWT handling, hashing, dependencies
  - **Configuration:** Environment variables

---

## 🧩 Applied Design Patterns

- **KISS:** Simple and direct code, easy to maintain.
- **DRY:** Reuse of common logic and utilities.
- **SOLID:** Separation of responsibilities in routes, controllers, and utilities.
- **YAGNI:** Only implement what is necessary for each functionality.

---

## 🔐 Security

- **JWT:** Authentication and authorization based on tokens.
- **Hashing:** Passwords stored and compared using bcrypt.
- **Validations:** Strong passwords and validated input data.
- **CORS:** Configurable according to the frontend origin.

---

## 📦 General Domain Structure



  ```
  users-auth/
  ├── register-user/
  ├── login-user/
  ├── change-password/
  ├── validate-token/
  └── README.md
  ```

  Each microservice contains its own source code, dependencies, configuration, and documentation.

  ---

  ## ⚙️ Execution and deployment

Each microservice can be executed and deployed independently, either locally or in Docker containers. See the README for each microservice for detailed instructions.

  ---
  :

  🐳 Deployment with Docker Compose
  To launch all microservices in the users-auth domain along with the database, use Docker Compose.
  This allows you to start and manage all services with a single command, facilitating development and deployment locally or on servers.

docker-compose up --build

  ## 📚 Notes

- The microservice architecture allows each component to be scaled, maintained, and deployed independently.
- The users-auth domain is essential for security and user management in **My Pet Host**.
- It complies with software engineering best practices to ensure clean, secure, and maintainable code.

---