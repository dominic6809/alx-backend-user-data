# 0x02-Session_authentication
# Session-Based Authentication System

This project implements a session-based authentication system with an expiration mechanism and session persistence using a database (file storage). The system includes basic and session authentication mechanisms with the ability to manage session durations and store session information across application restarts.

## Features
- **Session Authentication**: Allows users to authenticate using session IDs stored in memory or a database.
- **Session Expiration**: Sessions automatically expire after a defined duration.
- **Session Persistence**: Sessions are stored in a database (or file) to survive application restarts.
- **Logout**: Users can log out, which destroys their session.
  
## Models

### `User`
- Represents a user with basic details (email, password, etc.).
  
### `UserSession`
- Stores session-related information, including:
  - `user_id`: ID of the authenticated user.
  - `session_id`: Unique session identifier.
  - `created_at`: Timestamp when the session was created.

## Authentication Classes

### `SessionAuth`
- Basic authentication using session IDs stored in memory.
  
### `SessionExpAuth` (inherits from `SessionAuth`)
- Extends `SessionAuth` to add session expiration based on a configurable duration.
  
### `SessionDBAuth` (inherits from `SessionExpAuth`)
- Extends `SessionExpAuth` to store session data in a database (or file) instead of memory.
- Supports session creation, expiration, and destruction.

## Setup

### Environment Variables
- `AUTH_TYPE`: Choose the authentication type (`basic_auth`, `session_exp_auth`, or `session_db_auth`).
- `SESSION_NAME`: Name of the session cookie (default is `_my_session_id`).
- `SESSION_DURATION`: Duration in seconds before session expires (used for `SessionExpAuth` and `SessionDBAuth`).

### Install Dependencies
Ensure you have the necessary packages:
```bash
pip install flask
