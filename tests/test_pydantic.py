"""
https://pydantic-docs.helpmanual.io/
"""
from datetime import datetime
from typing import List, Optional
from decimal import Decimal

from pydantic import BaseModel, validator
from pydantic.dataclasses import dataclass


def test_basic():
    class User(BaseModel):
        id: int
        name = "John Doe"
        signup_ts: Optional[datetime] = None
        friends: List[int] = []

    external_data = {
        "id": "123",
        "signup_ts": "2019-06-01 12:22",
        "friends": [1, 2, "3"],
    }

    user = User(**external_data)

    assert user.id == 123
    assert user.name == "John Doe"
    assert user.signup_ts == datetime(2019, 6, 1, 12, 22)
    assert user.friends == [1, 2, 3]


def test_getitem():
    class User(BaseModel):
        id: int
        name = "John Doe"
        signup_ts: Optional[datetime] = None
        friends: List[int] = []

        # Make the class subscriptable.
        # https://stackoverflow.com/questions/62560890/how-to-make-custom-data-class-subscriptable
        def __getitem__(self, item):
            return getattr(self, item)

    external_data = {
        "id": "123",
        "signup_ts": "2019-06-01 12:22",
        "friends": [1, 2, "3"],
    }

    user = User(**external_data)

    assert user.id == 123
    assert user["id"] == 123


def test_validator():
    class User(BaseModel):
        age: str

        @validator("age")
        def validate_age(cls, v):
            if int(v) < 0:
                raise ValueError("Age must be positive")
            return int(v)

    user = User(age="1")
    assert user.age == 1
    assert type(user.age) == int
