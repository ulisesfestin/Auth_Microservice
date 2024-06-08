from app.models import RegisterRequest
from marshmallow import fields, Schema, post_load, validate


class RegisterSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    lastname = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    phone_number = fields.Str(required=True, validate=validate.Length(min=1, max=15))
    email_address = fields.Str(required=True, validate=validate.Email())
    password = fields.Str(required=True)

    @post_load
    def make_register_request(self, data, **kwargs):
        return RegisterRequest(**data)