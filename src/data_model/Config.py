# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = config_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Problem:
    part_1: str
    part_2: str

    def __init__(self, part_1: str, part_2: str) -> None:
        self.part_1 = part_1
        self.part_2 = part_2

    @staticmethod
    def from_dict(obj: Any) -> 'Problem':
        assert isinstance(obj, dict)
        part_1 = from_str(obj.get("part_1"))
        part_2 = from_str(obj.get("part_2"))
        return Problem(part_1, part_2)

    def to_dict(self) -> dict:
        result: dict = {"part_1": from_str(self.part_1), "part_2": from_str(self.part_2)}
        return result


class API:
    host: str
    problem: Problem
    token: str
    test_token: str

    def __init__(self, host: str, problem: Problem, token: str, test_token: str) -> None:
        self.host = host
        self.problem = problem
        self.token = token
        self.test_token = test_token

    @staticmethod
    def from_dict(obj: Any) -> 'API':
        assert isinstance(obj, dict)
        host = from_str(obj.get("host"))
        problem = Problem.from_dict(obj.get("problem"))
        token = from_str(obj.get("token"))
        test_token = from_str(obj.get("test_token"))
        return API(host, problem, token, test_token)

    def to_dict(self) -> dict:
        result: dict = {"host": from_str(self.host), "problem": to_class(Problem, self.problem),
                        "token": from_str(self.token), "test_token": from_str(self.test_token)}
        return result


class Mode:
    sample: str

    def __init__(self, sample: str) -> None:
        self.sample = sample

    @staticmethod
    def from_dict(obj: Any) -> 'Mode':
        assert isinstance(obj, dict)
        sample = from_str(obj.get("sample"))
        return Mode(sample)

    def to_dict(self) -> dict:
        result: dict = {"sample": from_str(self.sample)}
        return result


class Config:
    api: API
    mode: Mode

    def __init__(self, api: API, mode: Mode) -> None:
        self.api = api
        self.mode = mode

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        assert isinstance(obj, dict)
        api = API.from_dict(obj.get("API"))
        mode = Mode.from_dict(obj.get("mode"))
        return Config(api, mode)

    def to_dict(self) -> dict:
        result: dict = {"API": to_class(API, self.api), "mode": to_class(Mode, self.mode)}
        return result


def config_from_dict(s: Any) -> Config:
    return Config.from_dict(s)


def config_to_dict(x: Config) -> Any:
    return to_class(Config, x)
