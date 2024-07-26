from app.models import LoginRequest, RegisterRequest
from app.mapping import RegisterSchema
from tenacity import retry, stop_after_attempt, wait_random
import requests
import os

register_schema = RegisterSchema()

class AuthService:
    """
    Este servicio se encarga de manejar la lógica de negocio referida a la autenticación.
    """

    def register(self, register_data: RegisterRequest):
        mail_verification = self.get_user_by_email(register_data)

        if mail_verification.status_code == 200:
            return None
        else:
            try:
                self.register_user(register_data)
                return "Token"
            except:
                return None

    @retry(stop=stop_after_attempt(5), wait=wait_random(min=1, max=2))
    def register_user(self, register_data):
        requests.post(os.getenv('URL_CREATE_USER'), json=register_schema.dump(register_data))

    @retry(stop=stop_after_attempt(5), wait=wait_random(min=1, max=2))
    def get_user_by_email(self, data):
        if isinstance(data, LoginRequest):
            mail = data.email.replace('"', '').replace("'", "")
        elif isinstance(data, RegisterRequest):
            mail = data.email_address.replace('"', '').replace("'", "")
        request = requests.get(os.getenv('URL_FINDBYMAIL_USER').format(mail))
        return request

    def login(self, login_data: LoginRequest):
        mail_verification = self.get_user_by_email(login_data)

        if mail_verification.status_code == 200:
            mail = login_data.email.replace('"', '').replace("'", "")
            password = login_data.password.replace('"', '').replace("'", "")
            check_password = self.check_user_password(mail, password)
            if check_password.status_code != 200:
                return None
            return "Token"
        else:
            return None

    @retry(stop=stop_after_attempt(5), wait=wait_random(min=1, max=2))
    def check_user_password(self, mail, password):
        request = requests.get(os.getenv('URL_CHECKPASSWORD_USER').format(mail, password))
        return request
        