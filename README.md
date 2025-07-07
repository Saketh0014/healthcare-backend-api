
# 🏥 Healthcare Backend API

✅ To test all endpoints visually, visit: http://127.0.0.1:8000/swagger

This project is a backend system for a healthcare application built using Django, Django REST Framework (DRF), and PostgreSQL. It provides secure user registration, login, and full CRUD APIs for managing patients, doctors, and their mappings with JWT-based authentication.

---

## 🚀 Project Setup

### ✅ Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

### ⚙️ Installation Steps

1. **Navigate to the project directory**

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
source venv/bin/activate

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**

```env
# .env
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True
POSTGRES_DB=yourdbname
POSTGRES_USER=yourusername
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

> Note: When creating a superuser, the email address is optional and not required for Django admin login. You can leave the email blank during superuser creation.
POSTGRES_PORT=5432

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

App will be live at http://127.0.0.1:8000/

---

## 🔐 Authentication APIs

- `POST /api/auth/register/` – Register a new user
- `POST /api/auth/login/` – Login and obtain JWT tokens

---

## 🩺 Patient APIs (Authenticated)

- `GET /api/patients/` – List your patients
- `POST /api/patients/` – Add a patient
- `GET /api/patients/{id}/` – Patient detail
- `PUT /api/patients/{id}/` – Update patient
- `DELETE /api/patients/{id}/` – Delete patient

---

## 👨‍⚕️ Doctor APIs (Authenticated)

- `GET /api/doctors/` – List all doctors
- `POST /api/doctors/` – Add a doctor
- `GET /api/doctors/{id}/` – Doctor detail
- `PUT /api/doctors/{id}/` – Update doctor
- `DELETE /api/doctors/{id}/` – Delete doctor

---

## 🔗 Patient-Doctor Mapping APIs (Authenticated)

- `GET /api/mappings/` – List all mappings
- `POST /api/mappings/` – Assign a doctor to patient
- `GET /api/mappings/{patient_id}/` – Get mappings for patient
- `DELETE /api/mappings/{id}/` – Remove a mapping

---

## 🧪 Testing the API

### ✅ Swagger UI

Access the auto-generated UI and test the APIs easily:

🌐 http://127.0.0.1:8000/swagger

### ✅ Postman or Curl

Use Postman or Curl with JWT Bearer tokens:

```makefile
Authorization: Bearer <your_access_token>
```

---
## 📌 Notes

- PostgreSQL must be running with correct `.env` configuration.
- Uses JWT via `djangorestframework-simplejwt`.
- Swagger auto-doc available at `/swagger/`.
- Admin dashboard available at `/admin/` (superuser required).
- Patient records are user-specific.

---
## 🛠️ Admin Dashboard Usage

The Django admin dashboard is accessible at:

```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created via:

```bash
python manage.py createsuperuser
```

to log in.

In the admin dashboard, you can:

- Manage users, patients, doctors, and patient-doctor mappings.
- Add, edit, or delete records directly.
- Monitor and maintain the backend data easily.

This interface is useful for administrative tasks and data management during development and testing.

---

---

## 📬 Contact

For queries, feel free to reach out to the project maintainer or open an issue.
