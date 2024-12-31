import json
from dataclasses import dataclass
from typing import AnyStr

import pytest


@dataclass
class _Fixture:
    text: AnyStr
    key: AnyStr
    encrypted_text: AnyStr


@pytest.fixture()
def keyed_data():
    yield _Fixture(
        "a secret message",
        "6Jsv61H7fbkeIkRvUpnZ98fu",
        "zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C",
    )


@pytest.fixture()
def keyless_data():
    yield _Fixture(
        "empty key",
        "",
        "3JXAeKJAiYmtSKIUkoQgh64XvuM09NNis3X6YQLYRcE=",
    )


@pytest.fixture()
def json_keyed_data():
    yield _Fixture(
        json.dumps({"first_name": "John", "last_name": "Doe"}),
        "6Jsv61H7fbkeIkRvUpnZ98fu",
        "zLBGM41dAfA2JuIkVHRKa1NdwBm8w2pwunVEKlOmGjt7xmSihZxt92C9e0Y1e7vi5IHOWw1Y1l1z7oR5A69etg==",
    )


@pytest.fixture()
def json_keyless_data():
    yield _Fixture(
        json.dumps({"first_name": "John", "last_name": "Doe"}),
        "",
        "3JXAeKJAiYmtSKIUkoQghz+CJtJxNwoqP4TzcCedyCC8LsU2Kz8FbbW5tBRDHKtatHi9MdLqHIaPhwEI/Rx3sQ==",
    )
