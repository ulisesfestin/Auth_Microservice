from flask import jsonify, Blueprint, request
from app.dto import ResponseBuilder
from app.mapping import LoginSchema, RegisterSchema
from app.services import AuthService
from app.validators import validate_with

auth = Blueprint('auth', __name__)
auth_service = AuthService()
response = ResponseBuilder()
login_schema = LoginSchema()
register_schema = RegisterSchema()

@auth.route('/register', methods=['POST'])
@validate_with(RegisterSchema)
def register(validated_data):
    register_data = validated_data
    register = auth_service.register(register_data)
    if register:
        response.add_data(register).add_message('User registered successfully').add_status(200)
        return jsonify(response.build()), response.status_code
    else:
        response.add_message('User already exists').add_status(400)
        return jsonify(response.build()), response.status_code
    

@auth.route('/login', methods=['POST'])
@validate_with(LoginSchema)
def login(validated_data):
    login_data = validated_data
    login = auth_service.login(login_data)
    if login:
        response.add_data(login).add_message('User logged in successfully').add_status(200)
        return jsonify(response.build()), response.status_code
    else:
        response.add_message('Invalid credentials').add_status(400)
        return jsonify(response.build()), response.status_code
    