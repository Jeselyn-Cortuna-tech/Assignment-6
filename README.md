# Production-Ready Django Photo Album Management System

## Project Description
This project is a production-ready Photo Album Management System developed using Django. The application allows users to upload, manage, and organize photos using secure authentication and Role-Based Access Control (RBAC). Cloudinary is integrated for cloud-based image storage, while PostgreSQL is used as the production database.

## Features
- User Registration
- User Login and Logout
- Role-Based Access Control (RBAC)
- Upload Photos
- Edit Photos
- Delete Photos
- User-specific photo access
- Cloudinary image storage
- PostgreSQL database support
- Class-Based Views (CBVs)
- Render deployment support

## Technologies Used
- Python
- Django
- PostgreSQL
- Cloudinary
- HTML
- CSS
- Render

## Installation Guide

Clone the repository:

```bash
git clone <repository-link>
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file and add the following:

```env
SECRET_KEY=your_secret_key
DEBUG=False

DATABASE_URL=your_database_url

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

## System Architecture

- Frontend: HTML/CSS
- Backend: Django
- Database: PostgreSQL
- Media Storage: Cloudinary
- Deployment Platform: Render

## Author

Jeselyn Ann Cortuna