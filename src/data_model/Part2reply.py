# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = part2_reply_from_dict(json.loads(json_string))

from typing import List, Any, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Data:
    return_leg_ids: List[str]

    def __init__(self, return_leg_ids: List[str]) -> None:
        self.return_leg_ids = return_leg_ids

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        return_leg_ids = from_list(from_str, obj.get("return_leg_ids"))
        return Data(return_leg_ids)

    def to_dict(self) -> dict:
        result: dict = {"return_leg_ids": from_list(from_str, self.return_leg_ids)}
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


class Part2Reply:
    header: Header
    data: Data

    def __init__(self, header: Header, data: Data) -> None:
        self.header = header
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'Part2Reply':
        assert isinstance(obj, dict)
        header = Header.from_dict(obj.get("header"))
        data = Data.from_dict(obj.get("data"))
        return Part2Reply(header, data)

    def to_dict(self) -> dict:
        result: dict = {"header": to_class(Header, self.header), "data": to_class(Data, self.data)}
        return result


def part2_reply_from_dict(s: Any) -> Part2Reply:
    return Part2Reply.from_dict(s)


def part2_reply_to_dict(x: Part2Reply) -> Any:
    return to_class(Part2Reply, x)
