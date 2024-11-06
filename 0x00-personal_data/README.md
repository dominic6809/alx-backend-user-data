# 0x00-personal_data
This project implements secure logging and password management with the following key components:

## Key Features:
- **Logging with Redaction**: The `RedactingFormatter` class filters and obfuscates Personally Identifiable Information (PII) fields from log messages.
- **Database Connection**: Secure connection to a MySQL database using environment variables for credentials.
- **Password Hashing**: The project uses bcrypt to hash user passwords and validate them securely.

## Features Implemented:

### 1. **Redacting Formatter**
The `RedactingFormatter` class is used to redact sensitive fields in log messages (e.g., email, password). Fields are filtered using regular expressions.
- **Fields to redact**: PII such as `email`, `ssn`, and `password` are replaced with `***`.
- **Logging format**: The formatter outputs logs in a consistent `[HOLBERTON]` format with timestamp and filtered values.

### 2. **Database Connection (`get_db`)**
A secure database connection is established using environment variables for:
- `PERSONAL_DATA_DB_USERNAME` (default: `root`)
- `PERSONAL_DATA_DB_PASSWORD` (default: empty string)
- `PERSONAL_DATA_DB_HOST` (default: `localhost`)
- `PERSONAL_DATA_DB_NAME` (user-defined database name)

### 3. **Password Hashing and Validation**
- **`hash_password`**: Hashes a password using bcrypt with salt.
- **`is_valid`**: Validates if the provided password matches the hashed password stored in the database.

## Environment Variables:
To run the scripts securely, the following environment variables are required:
- `PERSONAL_DATA_DB_USERNAME`: Database username (default: `root`)
- `PERSONAL_DATA_DB_PASSWORD`: Database password (default: empty string)
- `PERSONAL_DATA_DB_HOST`: Database host (default: `localhost`)
- `PERSONAL_DATA_DB_NAME`: Database name

## Installation:
1. Install dependencies:
   ```bash
   pip3 install bcrypt mysql-connector-python
