from enum import Enum, IntEnum


class _StrEnum(str, Enum):
    @classmethod
    def to_list(cls) -> list[str]:
        return [item.value for item in cls]


class _IntEnum(IntEnum):
    @classmethod
    def to_list(cls) -> list[int]:
        return [item.value for item in cls]


class StringSizeEnum(_IntEnum):
    S = 10
    M = 25
    L = 100
    XL = 200


class TextSizeEnum(_IntEnum):
    S = 1000
    M = 5000
    L = 10000
