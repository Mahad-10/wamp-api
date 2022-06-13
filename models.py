import enum
import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

Base = declarative_base()


def generate_user_id():
    return ''.join(uuid.uuid4().__str__().split("-"))


class SnapType(enum.Enum):
    user = "user"
    system = "system"

    def __str__(self):
        return self.value


class User(Base):
    __tablename__ = "store_user"

    id = Column(Integer, primary_key=True)
    password = Column(String(50))
    last_login = Column(DateTime)
    username = Column(String(50), unique=True)
    full_name = Column(String(50))
    email = Column(String(50), unique=True)
    uid = Column(String(50))
    is_admin = Column(Boolean)
    is_superuser = Column(Boolean)
    is_active = Column(Boolean)
    is_staff = Column(Boolean)
    date_joined = Column(DateTime)
    password_reset_email_otp = Column(Integer)
    account_activation_sms_otp = Column(Integer)
    snaps = relationship("Snap")


class Snap(Base):
    __tablename__ = "store_snap"

    id = Column(Integer, primary_key=True)
    snap_format = Column(Integer, default=1)
    authority_id = Column(String(255), default="simplethings")
    revision = Column(Integer, default=1)
    series = Column(String(255), default="16")
    uid = Column(String(255), default=generate_user_id, unique=True)
    publisher_id = Column(Integer, ForeignKey('store_user.id'))
    # publisher = relationship("User", back_populates="snaps")
    name = Column(String(255), unique=True)
    timestamp = Column(DateTime)
    type = Column(ChoiceType(SnapType, impl=String(255)), default=SnapType.system)
