import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class UserGender(enum.Enum):
    male = "male"
    female = "female"
    other = "other"

    def __str__(self):
        return self.value


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(50))
    age = Column(Integer)
    email = Column(String(50), unique=True)
    gender = Column(ChoiceType(UserGender, impl=String(10)))
