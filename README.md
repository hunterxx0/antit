# antit

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
    - [Front-end](#Front-end)
    - [Back-end](#Back-end)
  - [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [API Documentation](#api-documentation)

## Introduction

The goal of this project is to create a simple web application for manually transcribing audio as part of the data collection and annotation process.

## Features

- Transcription of speech from audio segments into text.
- Focus on the annotation task, not speech recognition.
- Handling multiple annotators to ensure dataset completeness.

## Getting Started

### Prerequisites

#### Front-end:

- bootstrap
- bootstrap-icons
- core-js
- jquery
- jwt-decode
- popper.js
- vue
- vue-router

#### Back-end:

- django
- django-cors-headers
- django-environ
- djangorestframework
- djangorestframework_simplejwt
- pytest
- psycopg2-binary
- requests
- responses

### Installation

Start by building the project using `docker-compose up --build`

## Usage

Begin by signing up and logging in. Afterward, you can add audio files and annotate them.

## Technology Stack

- Django (Python web framework) - Backend
- VueJs - Frontend
- PostgreSQL - Database backend
- Django REST framework - API endpoints

## API Documentation

[Audio](http://localhost:8000/api/audio/audio/)

[transcriptions](http://localhost:8000/api/transcription/1/transcriptions/)

[Update transcriptions](http://localhost:8000/api/transcription/1/transcription/update/1/)
