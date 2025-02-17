# Investor Information App
This repository contains a web application built with Python/FastAPI for the backend and React/JS for the frontend. The application allows users to view and search for investors, displaying information either in summary form or in more detail per investor.

## Features
- Investor Summary View: Provides a list of investors with brief summary information.

- Investor Detail View: Allows users to click on an investor to view more detailed information.

## Setup

### Backend:
`python -m venv venv`

`source venv/bin/activate`  

`pip install -r requirements.txt`

To run:

`cd FastAPI`

`uvicorn app.main:app --reload`

### Frontend:
`cd React/investors`

`npm install`

To run:

`npm start`

Usage:

Navigate to `http://localhost:3000` to view the application.


