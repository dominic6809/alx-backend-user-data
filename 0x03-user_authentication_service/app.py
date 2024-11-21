#!/usr/bin/env python3
"""
Main file
"""
from flask import Flask, request, jsonify, abort, redirect, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route('/')
def home():
    """
    Home route to check the API status
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def register_user():
    """
    Register a new user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(400, description="Missing email or password")

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"})

@app.route('/sessions', methods=['POST'])
def login():
    """
    Login a user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(400, description="Missing email or password")

    if not AUTH.valid_login(email, password):
        abort(401, description="Invalid credentials")

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response

@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    Logout a user
    """
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403, description="Session not found")

    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403, description="Invalid session")

    AUTH.destroy_session(user.id)
    return redirect('/')

@app.route('/profile', methods=['GET'])
def profile():
    """
    Get the profile of a user
    """
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403, description="Session not found")

    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403, description="Invalid session")

    return jsonify({"email": user.email})

@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """
    Generate a reset password token
    """
    email = request.form.get('email')

    if not email:
        abort(400, description="Missing email")

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403, description="Email not registered")

    return jsonify({"email": email, "reset_token": reset_token})

@app.route('/reset_password', methods=['PUT'])
def update_password():
    """
    Update the user's password using reset token
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    if not email or not reset_token or not new_password:
        abort(400, description="Missing required fields")

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403, description="Invalid reset token")

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
