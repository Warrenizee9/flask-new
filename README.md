# Flask API Assignment - CS 421

This is a simple Flask API developed and deployed as part of the **CS 421 - Application Deployment and Management** course.

## 🔧 Project Description

The goal of this assignment is to:
- Practice version control using Git and GitHub.
- Create a RESTful API using Flask with two endpoints.
- Deploy the API to an AWS Ubuntu server using a web server like Nginx.

## 📌 Endpoints

### 1. `/students`
- Returns a JSON array with at least 10 students.
- Each student includes:
  - `name`
  - `program` (e.g., BSc in Software Engineering)

Example:
```json
[
  {"name": "Alice", "program": "Software Engineering"},
  {"name": "Bob", "program": "Software Engineering"}
]
