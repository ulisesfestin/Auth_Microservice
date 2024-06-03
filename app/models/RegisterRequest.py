from dataclasses import dataclass


@dataclass
class RegisterRequest:
    name: str
    lastname: str
    phone_number: str
    email_address: str
    password: str