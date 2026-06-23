# TAG - Social Media Platform

TAG is a full-stack social media platform built using Django. The application enables users to connect, share posts, interact through comments and likes, and follow other users. The platform features a modern Pine Green themed responsive UI with Dark/Light mode support.

## Live Demo

https://tag-av2m.onrender.com/

---

## Features

### Authentication & User Profiles

* Secure User Registration and Login
* Automatic Profile Creation using Django Signals
* Edit Profile functionality
* Upload Profile Pictures
* Email Privacy Settings

### Social Features

* Create, Edit, and Delete Posts
* Upload Images with Posts
* Like and Unlike Posts
* Comment on Posts
* Edit and Delete Comments
* Follow and Unfollow Users
* User Search Functionality

### Feed System

* Global Feed displaying all posts
* Personalized Feed showing posts from followed users
* Post Detail Page with complete interactions

### UI/UX Features

* Responsive Design for Desktop and Mobile
* Modern Pine Green and Cream Theme
* Dark/Light Mode Toggle
* Interactive Hover Effects
* Default Profile Avatar

---

## Project Structure

```text
TAG/
├── TAG/                  # Project settings and root configuration
├── users/                # Authentication and profile management
├── posts/                # Post management system
├── interactions/         # Likes, comments, and follows
├── templates/            # HTML templates
├── static/               # CSS and JavaScript files
├── media/                # Uploaded images
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
```

---

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* JavaScript
* SQLite3
* Render (Deployment)
* Git & GitHub

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/gopikabonthu/codealpha_social-media.git
cd codealpha_social-media
```

### 2. Create and Activate Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Future Enhancements

* Real-time Notifications
* Direct Messaging System
* Hashtags and Mentions
* Story Feature
* Real-time Chat using WebSockets

---

## Developed For

CodeAlpha Internship Project

---

## Author

**Gopika Bonthu**
