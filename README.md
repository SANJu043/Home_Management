# 🗂️ LifeFlow — Personal Management Web App

LifeFlow is a personal productivity and management platform built with Django. It integrates essential tools like a to-do list, expense tracker, notes app, calendar, and inventory system — all under one dashboard.

---
(fhub had full basic app)

## 🚀 Features

- ✅ **To-Do List** — Track your tasks and daily goals
- 🧾 **Expense Tracker** — Manage and view your spending
- 🗒️ **Notes App** — Write, edit, and organize notes
- 📅 **Calendar** — Add events and plan your schedule
- 📦 **Inventory Management** — Log and monitor your items
- 🔐 **Authentication** — Secure signup/login using Django Auth

---
## 🛠️ Stack Used

Backend: Django  
Frontend: HTML, CSS (via Django Templates)  
Database: SQLite  
Authentication: Django's built-in auth system  

## 🏗️ Project Structure

fhub/
├── core/ # Main application module  
│   ├── admin.py # Admin dashboard setup   
│   ├── apps.py # App config  
│   ├── forms.py # Form classes for user input  
│   ├── models.py # Database models  
│   ├── urls.py # URL routes  
│   ├── views.py # Core views and logic  
│   ├── templates/ # HTML Templates  
│   │ ├── calendar.html  
│   │ ├── expenses.html  
│   │ ├── home.html  
│   │ ├── inventory.html  
│   │ ├── landing.html  
│   │ ├── login.html  
│   │ ├── notes.html  
│   │ ├── signup.html  
│   │ └── todo.html  
│   ├── migrations/ # Database schema migrations  
│   └── init.py  
├── db.sqlite3 # SQLite database  
├── fhub/ # Project configuration  
│   ├── settings.py # Django settings  
│   ├── urls.py # Root URLs  
│   ├── wsgi.py  
│   ├── asgi.py  
│   └── init.py  
└── manage.py # Django command-line utility  

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
-> git clone https://github.com/SANJu043/Home_Management
-> cd fhub
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
On mac: source venv/bin/activate
On Windows: venv\Scripts\activate
```
### 3. install django
```bash
pip install django
```
### 4. run the project
(use python3 if you have)  
```bash
python manage.py migrate
python manage.py runserver
```

Then go to http://127.0.0.1:8000/ in your browser.  
