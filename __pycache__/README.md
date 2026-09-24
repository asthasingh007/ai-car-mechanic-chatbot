# AI Car Mechanic Chatbot

A web-based AI Car Mechanic chatbot that helps car owners describe vehicle problems, receive basic troubleshooting guidance, upload car media, generate a diagnosis, and book a mechanic.

## Features

- Interactive car mechanic chatbot
- Car problem troubleshooting
- Diagnosis API
- Image, audio and video upload
- Mechanic booking
- Booking status API
- SQLite database
- React frontend
- Django REST Framework backend

## Technology Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/chat/` | Send car problem to chatbot |
| POST | `/api/upload/` | Upload car media |
| POST | `/api/diagnosis/` | Generate diagnosis |
| POST | `/api/booking/` | Create mechanic booking |
| GET | `/api/booking/{id}/` | Get booking details |

## How to Run Backend

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install django djangorestframework
python manage.py migrate
python manage.py runservergit add .git add .


git add .git status



