# 0x03-user_authentication_service
# User Authentication Service

This project is an implementation of a user authentication service that provides functionalities such as user registration, login, password reset, and session management. It is built with Python using Flask, SQLAlchemy, and other libraries to handle user data and authentication.

## Features

- User registration (`POST /users`)
- User login (`POST /sessions`)
- User logout (`DELETE /sessions`)
- Password reset functionality
- Profile retrieval for logged-in users
- Session management using cookies
- Password hashing and reset token handling

## Technologies Used

- **Flask**: A micro web framework for Python.
- **SQLAlchemy**: ORM for database interactions.
- **Flask-Login**: Provides user session management.
- **UUID**: Used for generating session IDs and reset tokens.
- **Werkzeug**: Used for hashing passwords.
- **Requests**: HTTP library for testing the endpoints.

## Project Structure
user_authentication_service │ ├── app.py # Main Flask application ├── auth.py # Authentication logic (register, login, password reset) ├── models.py # Database models for User and other entities ├── main.py # Script to test all the functionalities ├── requirements.txt # Python dependencies ├── venv/ # Virtual environment directory └── README.md # Project documentation (this file)


## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-url.git

## Testing the Application
To test the functionalities, the main.py module is provided, which automates the following tasks:

Register a new user.

Attempt to log in with incorrect credentials.

View profile of an unlogged user.

Log in with valid credentials and view the profile.

Log out and verify.

Request a reset password token.

Update the user's password and verify.

Run the tests using:
```
    python main.py
```
## Licence
### MIT License

Copyright (c) [2024] Dominic Muuo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
