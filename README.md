# AI Car Mechanic Chatbot

An AI-powered car mechanic chatbot that helps car owners troubleshoot common vehicle problems and book a mechanic.

## Features

- Car problem chat interface
- Rule-based mechanical troubleshooting
- Car media upload
- Diagnosis generation
- Mechanic booking
- Booking status API
- REST APIs using Django REST Framework

## Technologies

### Frontend
- React
- Vite
- HTML
- CSS
- JavaScript

### Backend
- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

- POST `/api/chat/`
- POST `/api/upload/`
- POST `/api/diagnosis/`
- POST `/api/booking/`
- GET `/api/booking/{id}/`

## Project Structure

- `frontend/` - React frontend
- `chatbot/` - Django chatbot application
- `config/` - Django project configuration
- `media/` - Uploaded media files
- `manage.py` - Django management file

## How to Run

### Backend

```bash
python manage.py runserver
