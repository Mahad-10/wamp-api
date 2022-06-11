from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UserSchema(SQLAlchemyAutoSchema):
    id = fields.Int()
    password = fields.String()
    last_login = fields.DateTime()
    username = fields.String()
    full_name = fields.String()
    email = fields.Email()
    uid = fields.String()
    is_admin = fields.Boolean()
    is_superuser = fields.Boolean()
    is_active = fields.Boolean()
    is_staff = fields.Boolean()
    date_joined = fields.DateTime()
    password_reset_email_otp = fields.Int()
    account_activation_sms_otp = fields.Int()


class SnapSchema(SQLAlchemyAutoSchema):
    snap_format = fields.Int()
    authority_id = fields.String()
    revision = fields.Int()
    series = fields.String()
    uid = fields.String()
    publisher = fields.String()
    name = fields.String()
    timestamp = fields.DateTime()
    type = fields.String()
