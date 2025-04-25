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
## Assignment 2 - Bash Automation & Monitoring

This part of the project extends the Flask API deployment from Assignment 1 by adding system automation and monitoring using Bash scripting and Linux cron jobs.

### 📁 Bash Scripts

Three scripts were created and stored in the `bash_scripts/` folder:

1. **health_check.sh**  
   - Logs CPU, memory, disk usage, and confirms the Flask API is reachable.
   - Output is saved to `/var/log/server_health.log`.

2. **backup_api.sh**  
   - Creates a `.tar.gz` backup of the Flask project and removes backups older than 7 days.
   - Saves backups in `/home/ubuntu/backups`.

3. **update_server.sh**  
   - Runs `apt update`, pulls the latest code from GitHub, and restarts the Flask API service.
   - Logs are saved to `/var/log/update.log`.

### 🔁 Cron Jobs

The scripts are scheduled using `crontab` as follows:

| Script             | Schedule                   |
|--------------------|----------------------------|
| `health_check.sh`  | Every 6 hours              |
| `backup_api.sh`    | Daily at 2:00 AM           |
| `update_server.sh` | Every 3 days at 3:00 AM    |

Cron proof included in `cron_setup.txt`.

### 📄 Sample Logs

Logs from health checks and updates were combined and included in `logs_sample.txt`.

### ✅ Result

This automation setup ensures that the API server is:
- Regularly monitored
- Automatically backed up
- Always running with the latest updates

All files are available in this repository.
### 🐳 Docker Image Backup (WeTransfer)

If Docker Hub is inaccessible, you can download the Docker image from the link below:

🔗 [Download flask-api-assignment3.tar.gz](https://we.tl/t-0aS2ATSzEP)

