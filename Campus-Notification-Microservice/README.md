# Campus Notification Microservice

## Objective

Develop a campus notification system that fetches notifications from the provided API and displays the top 10 unread notifications based on priority.

---

## Features

- Fetch notifications using REST API
- Calculate notification priority
- Sort notifications by priority
- Display Top 10 notifications
- Logging middleware

---

## Technologies

- Python 3
- Requests
- Datetime
- Logging

---

## Project Structure

```
Campus-Notification-Microservice/
│
├── app.py
├── priority_inbox.py
├── logger.py
├── requirements.txt
├── README.md
├── screenshots/
└── logs/
```

---

## Run

Install dependencies

```
pip install -r requirements.txt
```

Run

```
python app.py
```

---

## Priority Calculation

Placement = 30

Result = 20

Event = 10

Recency = 20 - Minutes Old

Priority Score

```
Priority = Type Weight + Recency
```

---

## Logging

Every API request and response is recorded in

```
logs/app.log
```