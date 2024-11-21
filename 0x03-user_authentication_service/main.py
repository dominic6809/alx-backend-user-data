#!/usr/bin/env python3
"""
Main script to interact with the user authentication service.

This script performs various tasks such as:
1. Registering a user
2. Logging in with incorrect and correct credentials
3. Accessing the user's profile with and without being logged in
4. Logging out
5. Requesting a password reset token and updating the password

The script uses the `requests` module to send HTTP requests
to the Flask app and validates the responses using assertions.
"""

import requests


BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """
    Register a new user by sending a POST request to the /users endpoint.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Raises:
        AssertionError: If the response status code
        or JSON payload is incorrect.
    """
    url = "{}/users".format(BASE_URL)
    body = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=body)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}
    res = requests.post(url, data=body)
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Attempt to log in with incorrect credentials.

    Args:
        email (str): The email of the user.
        password (str): The incorrect password.

    Raises:
        AssertionError: If the response status code is not 401.
    """
    url = "{}/sessions".format(BASE_URL)
    body = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=body)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Log in a user and return the session ID.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        str: The session ID from the response cookies.

    Raises:
        AssertionError: If the response status code is incorrect
        or session_id is missing.
    """
    url = "{}/sessions".format(BASE_URL)
    body = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=body)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "logged in"}
    return res.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    Attempt to access the profile of a user without being logged in.

    Raises:
        AssertionError: If the response status code is not 403.
    """
    url = "{}/profile".format(BASE_URL)
    res = requests.get(url)
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Access the profile of a logged-in user using the session ID.

    Args:
        session_id (str): The session ID of the logged-in user.

    Raises:
        AssertionError: If the response status code is not 200
        or the email is missing from the response.
    """
    url = "{}/profile".format(BASE_URL)
    req_cookies = {
        'session_id': session_id,
    }
    res = requests.get(url, cookies=req_cookies)
    assert res.status_code == 200
    assert "email" in res.json()


def log_out(session_id: str) -> None:
    """
    Log out the user by destroying the session.

    Args:
        session_id (str): The session ID of the logged-in user.

    Raises:
        AssertionError: If the response status code is not 302 (redirect).
    """
    url = "{}/sessions".format(BASE_URL)
    req_cookies = {
        'session_id': session_id,
    }
    res = requests.delete(url, cookies=req_cookies)
    assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """
    Request a reset password token for the user.

    Args:
        email (str): The email of the user.

    Returns:
        str: The reset token received in the response.

    Raises:
        AssertionError: If the response status code is not 200
        or reset_token is missing.
    """
    url = "{}/reset_password".format(BASE_URL)
    body = {'email': email}
    res = requests.post(url, data=body)
    assert res.status_code == 200
    assert "email" in res.json()
    assert res.json()["email"] == email
    assert "reset_token" in res.json()
    return res.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Update the user's password using a reset token.

    Args:
        email (str): The email of the user.
        reset_token (str): The reset token provided to the user.
        new_password (str): The new password to set.

    Raises:
        AssertionError: If the response status code is not 200
        or the expected message is incorrect.
    """
    url = "{}/reset_password".format(BASE_URL)
    body = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password,
    }
    res = requests.put(url, data=body)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    """
    Main function to execute the tasks in sequence.

    - Registers the user
    - Tries logging in with wrong password
    - Accesses the profile without being logged in
    - Logs in with correct password and accesses profile
    - Logs out
    - Resets password and updates the user's password
    - Logs in with the new password
    """
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
