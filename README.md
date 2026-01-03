<div align="center">
  
# Learning Management System (LMS)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
</div>

> This LMS is designed for students of Section A. It supports account creation, login, and interactive dashboard sections for managing assignments, quizzes, attendance, timetable, and courses.
---

##  Team Members
**Section:** BA  
**Semester:** 1 (Evening)  
**Subject:** Programming Fundamentals  

| Member Name        | Roll Number | Role     | Contribution                                           |
|-------------------|------------|---------|-------------------------------------------------------|
| **Bilal**    | 161        | Frontend | Login & Auth UI (`index.html`)                        |
| **Beenish Majeed**    | 058        | Frontend | Dashboard & Activities UI (`dashboard.html`)          |
| **Saad Shah** | 121    | Backend  | Flask Logic & Session Management (`backend.py`, `backend2.py`) |
 
---

## Project Overview

The Learning Management System (LMS) is a beginner-friendly web project built using **Python Flask** for backend logic and **HTML/CSS** for the frontend interface.  
It focuses on session handling, UI design, and basic student activity management.

---

## Features

- **Secure Auth:** Session-based login and account creation  
- **Activity Section:** Sections for Assignments, Quizzes, and Attendance
<div align="center">
<img width="1445" height="740" alt="Screenshot 2025-12-30 205850" src="https://github.com/user-attachments/assets/d88a1dd1-5b47-4368-807a-e3d218e23b65" />
<p style="font-size: 0.9rem; color: #555; text-align:center; margin-top:5px;"> <strong><em>Activity section of the LMS project</em></strong></p>
</div>

- **Schedule Management:** Interactive timetable to view class timings  
- **Course Insights:** Quick view of enrolled courses and assigned teachers  
- **GUI:** Clean and user-friendly interface  
- **Frontend & Backend Separation:** HTML/CSS for frontend, Flask + Python for backend  

---

## How It Works

1. User creates an account (Full Name, Email as username, Password) 
2. Login using Email & Password

<div align="center">
<img width="1445" height="740" alt="Screenshot 2025-12-30 224022" src="https://github.com/user-attachments/assets/b63e8684-7960-4baa-ac72-d5a85fefce13" />
<p style="font-size: 0.9rem; color: #555; text-align:center; margin-top:5px;"> <strong><em>Login page: enter your credentials to access the LMS</em></strong></p>
</div> 

3. Session is created to maintain user login  
4. User sees a full-page dashboard after login  
5. Sections (Assignments, Courses, Attendance, Timetable) can be expanded to view content
<div align="center"> 
 <img width="1415" height="758" alt="Screenshot 2025-12-30 205825" src="https://github.com/user-attachments/assets/982abdc5-062d-49ae-9abd-8dafdc207fd0" />
<p style="font-size: 0.9rem; color: #555; text-align:center; margin-top:5px;"> <strong><em>Timetable section: view your class schedule and timings</em></strong></p>
</div> 

---

## File Structure

| File / Folder | Type | Description |
|---------------|------|------------|
| `backend.py` | Python | Handles backend logic (account creation, login, session management) |
| `backend2.py` | Python | Optional route definitions / main entry point |
| `run.py` | Python | Run Flask application |
| `users.json` | JSON | Stores user data (email, password, name, role) |
| `templates/index.html` | HTML | Login & Create Account page |
| `templates/dashboard.html` | HTML | Dashboard after login with sections |
| `static/style.css` | CSS | Login page styling |
| `static/dashboard.css` | CSS | Dashboard page styling |

---
## Run Instructions

```bash
# 1. Clone the repository
git clone <repository-link>

# 2. Navigate into the project folder
cd <repository-folder>

# 3. Install Flask (if not already installed)
pip install flask

# 4. Run the application
python run.py

5. Open the application in your browser
Go to: http://127.0.0.1:5000/

