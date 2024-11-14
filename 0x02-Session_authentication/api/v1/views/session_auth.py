#!/usr/bin/env python3
"""
Session authentication views for handling login and logout
"""
from flask import Blueprint, request, jsonify, make_response, abort
from api.v1.app import auth
from models.user import User

session_auth_view = Blueprint('session_auth', __name__, url_prefix='/api/v1/auth_session')

@session_auth_view.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """
    POST /auth_session/login: Logs in the user by creating a session.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create session
    session_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    response.set_cookie(auth.session_name, session_id)

    return response

@session_auth_view.route('/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    DELETE /auth_session/logout: Logs out the user by destroying the session.
    """
    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
