# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = part1_reply_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast

T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Data:
    total_seconds: int

    def __init__(self, total_seconds: int) -> None:
        self.total_seconds = total_seconds

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        total_seconds = from_int(obj.get("total_seconds"))
        return Data(total_seconds)

    def to_dict(self) -> dict:
        result: dict = {"total_seconds": from_int(self.total_seconds)}
        return result


class Header:
    token: str

    def __init__(self, token: str) -> None:
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'Header':
        assert isinstance(obj, dict)
        token = from_str(obj.get("token"))
        return Header(token)

    def to_dict(self) -> dict:
        result: dict = {"token": from_str(self.token)}
        return result


class Part1Reply:
    header: Header
    data: Data

    def __init__(self, header: Header, data: Data) -> None:
        self.header = header
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'Part1Reply':
        assert isinstance(obj, dict)
        header = Header.from_dict(obj.get("header"))
        data = Data.from_dict(obj.get("data"))
        return Part1Reply(header, data)

    def to_dict(self) -> dict:
        result: dict = {"header": to_class(Header, self.header), "data": to_class(Data, self.data)}
        return result


def part1_reply_from_dict(s: Any) -> Part1Reply:
    return Part1Reply.from_dict(s)


def part1_reply_to_dict(x: Part1Reply) -> Any:
    return to_class(Part1Reply, x)
