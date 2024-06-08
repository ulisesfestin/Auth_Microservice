from app.models import LoginRequest, RegisterRequest
from app.mapping import RegisterSchema
import requests

register_schema = RegisterSchema()

class AuthService:
    """
    Este servicio se encarga de manejar la lógica de negocio referida a la autenticación.
    """

    def register(self, register_data: RegisterRequest):
        mail = register_data.email_address.replace('"', '').replace("'", "")
        request = requests.get('http://user.um.localhost:5000/api/v1/user/findbymail/{}'.format(mail))

        if request.status_code == 200:
            return None
        else:
            requests.post('http://user.um.localhost:5000/api/v1/user/create', json=register_schema.dump(register_data))
            return "Token"

    def login(self, login_data: LoginRequest):
        mail = login_data.email.replace('"', '').replace("'", "")
        request = requests.get('http://user.um.localhost:5000/api/v1/user/findbymail/{}'.format(mail))

        if request.status_code == 200:
            password = login_data.password.replace('"', '').replace("'", "")
            check_password = requests.get('http://user.um.localhost:5000/api/v1/user/checkpassword/{}/{}'.format(mail, password))
            if check_password.status_code == 200:
                return "Token"
            else:
                return None
        else:
            return None
        