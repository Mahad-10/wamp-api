from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UserSchema(SQLAlchemyAutoSchema):
    email = fields.Email()
    fullname = fields.Str()
    age = fields.Int()
    gender = fields.String()
