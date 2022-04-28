"""
https://pydantic-docs.helpmanual.io/
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


def test_basic():
    class User(BaseModel):
        id: int
        name = 'John Doe'
        signup_ts: Optional[datetime] = None
        friends: List[int] = []


    external_data = {
        'id': '123',
        'signup_ts': '2019-06-01 12:22',
        'friends': [1, 2, '3'],
    }

    user = User(**external_data)

    assert user.id == 123
    assert user.name == 'John Doe'
    assert user.signup_ts == datetime(2019, 6, 1, 12, 22)
    assert user.friends == [1, 2, 3]

