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
