# E-Commerce API with Django Rest Framework

Welcome to the **E-Commerce API** project! This repository contains a backend application built using Django and Django Rest Framework, designed to provide a robust API for an e-commerce platform. The API supports various functionalities necessary for managing an online store, including product management, user authentication, and order processing.

## Features

- **User Authentication**: Register, login, and manage user accounts with token-based authentication.
- **Product Management**: Create, update, delete, and view products with detailed information.
- **Category Management**: Organize products into categories for better navigation.
- **Cart and Order Management**: Add products to the cart, create orders, and track order status.
- **Admin Panel**: Manage the platform using Django's built-in admin interface.

## Technologies Used

- **Django**: High-level Python web framework.
- **Django Rest Framework**: Powerful and flexible toolkit for building Web APIs.
- **SQLite**: Default database for development (can be switched to PostgreSQL or MySQL for production).
- **JWT**: JSON Web Token for user authentication.

## Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/GioKhoma/Rest_Framework.git

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   
3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   
4. **Apply migrations**:
   ```sh
   python manage.py migrate

5. **Run the development server**:
   ```sh
   python manage.py runserver

### Access the API documentation:
- Navigate to http://127.0.0.1:8000/swagger/ in your web browser to view the API documentation.

