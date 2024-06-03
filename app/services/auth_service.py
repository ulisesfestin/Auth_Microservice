from app.models import LoginRequest, RegisterRequest
from app.services.security_service import SecurityService
import requests


class AuthService:
    """
    Este servicio se encarga de manejar la lógica de negocio referida a la autenticación.
    """

    def register(self, register_data: RegisterRequest):
        request = requests.get('http://user.um.localhost:5000/api/v1/user/findbymail/{}'.format(register_data.email_address))

        if request.status_code == 200:
            return None
        else:
            requests.post('http://user.um.localhost:5000/api/v1/user/create', json=register_data)
            return "Token"

    def login(self, login_data: LoginRequest):
        request = requests.get('http://user.um.localhost:5000/api/v1/user/findbymail/{}'.format(login_data.email_address))

        if request.status_code == 200 and SecurityService.check_password(request.password, login_data.password):
            return "Token"
        else:
            return None
        