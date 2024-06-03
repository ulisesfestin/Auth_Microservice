from app.models import LoginRequest
from marshmallow import fields, Schema, post_load, validate


class LoginSchema(Schema):
    email = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True, validate=validate.Length(min=1, max=25))

    @post_load
    def make_login_request(self, data, **kwargs):
        return LoginRequest(**data)