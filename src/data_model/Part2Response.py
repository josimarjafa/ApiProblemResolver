from typing import Any, List, TypeVar, Type, cast, Callable
from enum import Enum
from datetime import datetime
import dateutil.parser

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_none(x: Any) -> Any:
    assert x is None
    return x


class Arguments:
    outbound_leg_id: str

    def __init__(self, outbound_leg_id: str) -> None:
        self.outbound_leg_id = outbound_leg_id

    @staticmethod
    def from_dict(obj: Any) -> 'Arguments':
        assert isinstance(obj, dict)
        outbound_leg_id = from_str(obj.get("outbound_leg_id"))
        return Arguments(outbound_leg_id)

    def to_dict(self) -> dict:
        result: dict = {"outbound_leg_id": from_str(self.outbound_leg_id)}
        return result


class Data:
    return_leg_ids: str

    def __init__(self, return_leg_ids: str) -> None:
        self.return_leg_ids = return_leg_ids

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        return_leg_ids = from_str(obj.get("return_leg_ids"))
        return Data(return_leg_ids)

    def to_dict(self) -> dict:
        result: dict = {"return_leg_ids": from_str(self.return_leg_ids)}
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


class ExpectedReturnShape:
    header: Header
    data: Data

    def __init__(self, header: Header, data: Data) -> None:
        self.header = header
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'ExpectedReturnShape':
        assert isinstance(obj, dict)
        header = Header.from_dict(obj.get("header"))
        data = Data.from_dict(obj.get("data"))
        return ExpectedReturnShape(header, data)

    def to_dict(self) -> dict:
        result: dict = {"header": to_class(Header, self.header), "data": to_class(Data, self.data)}
        return result


class Fare:
    id: str
    legs: List[str]

    def __init__(self, id: str, legs: List[str]) -> None:
        self.id = id
        self.legs = legs

    @staticmethod
    def from_dict(obj: Any) -> 'Fare':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        legs = from_list(from_str, obj.get("legs"))
        return Fare(id, legs)

    def to_dict(self) -> dict:
        result: dict = {"id": from_str(self.id), "legs": from_list(from_str, self.legs)}
        return result


class Airline:
    code: str
    name: str
    short_name: str

    def __init__(self, code: str, name: str, short_name: str) -> None:
        self.code = code
        self.name = name
        self.short_name = short_name

    @staticmethod
    def from_dict(obj: Any) -> 'Airline':
        assert isinstance(obj, dict)
        code = from_str(obj.get("code"))
        name = from_str(obj.get("name"))
        short_name = from_str(obj.get("short_name"))
        return Airline(code, name, short_name)

    def to_dict(self) -> dict:
        result: dict = {"code": from_str(self.code), "name": from_str(self.name),
                        "short_name": from_str(self.short_name)}
        return result


class Airport:
    state: str
    state_code: str
    name: str
    code: str

    def __init__(self, state: str, state_code: str, name: str, code: str) -> None:
        self.state = state
        self.state_code = state_code
        self.name = name
        self.code = code

    @staticmethod
    def from_dict(obj: Any) -> 'Airport':
        assert isinstance(obj, dict)
        state = from_str(obj.get("state"))
        state_code = from_str(obj.get("state_code"))
        name = from_str(obj.get("name"))
        code = from_str(obj.get("code"))
        return Airport(state, state_code, name, code)

    def to_dict(self) -> dict:
        result: dict = {"state": from_str(self.state), "state_code": from_str(self.state_code),
                        "name": from_str(self.name), "code": from_str(self.code)}
        return result


class UTC:
    iso: datetime

    def __init__(self, iso: datetime) -> None:
        self.iso = iso

    @staticmethod
    def from_dict(obj: Any) -> 'UTC':
        assert isinstance(obj, dict)
        iso = from_datetime(obj.get("iso"))
        return UTC(iso)

    def to_dict(self) -> dict:
        result: dict = {"iso": self.iso.isoformat()}
        return result


class Leg:
    id: str
    airline: Airline
    flight_number: int
    departure_airport: Airport
    arrival_airport: Airport
    departure_utc: UTC
    arrival_utc: UTC

    def __init__(self, id: str, airline: Airline, flight_number: int, departure_airport: Airport,
                 arrival_airport: Airport, departure_utc: UTC, arrival_utc: UTC) -> None:
        self.id = id
        self.airline = airline
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_utc = departure_utc
        self.arrival_utc = arrival_utc

    @staticmethod
    def from_dict(obj: Any) -> 'Leg':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        airline = Airline.from_dict(obj.get("airline"))
        flight_number = int((obj.get("flight_number")))
        departure_airport = Airport.from_dict(obj.get("departure_airport"))
        arrival_airport = Airport.from_dict(obj.get("arrival_airport"))
        departure_utc = UTC.from_dict(obj.get("departure_utc"))
        arrival_utc = UTC.from_dict(obj.get("arrival_utc"))
        return Leg(id, airline, flight_number, departure_airport, arrival_airport, departure_utc, arrival_utc)

    def to_dict(self) -> dict:
        result: dict = {"id": from_str(self.id), "airline": to_class(Airline, self.airline),
                        "flight_number": from_str(str(self.flight_number)),
                        "departure_airport": to_class(Airport, self.departure_airport),
                        "arrival_airport": to_class(Airport, self.arrival_airport),
                        "departure_utc": to_class(UTC, self.departure_utc),
                        "arrival_utc": to_class(UTC, self.arrival_utc)}
        return result


class Input:
    fares: List[Fare]
    legs: List[Leg]

    def __init__(self, fares: List[Fare], legs: List[Leg]) -> None:
        self.fares = fares
        self.legs = legs

    @staticmethod
    def from_dict(obj: Any) -> 'Input':
        assert isinstance(obj, dict)
        fares = from_list(Fare.from_dict, obj.get("fares"))
        legs = from_list(Leg.from_dict, obj.get("legs"))
        return Input(fares, legs)

    def to_dict(self) -> dict:
        result: dict = {"fares": from_list(lambda x: to_class(Fare, x), self.fares),
                        "legs": from_list(lambda x: to_class(Leg, x), self.legs)}
        return result


class Part2Response:
    token: str
    description: str
    arguments: Arguments
    expected_return_shape: ExpectedReturnShape
    millisecond_time_limit: None
    input: Input

    def __init__(self, token: str, description: str, arguments: Arguments, expected_return_shape: ExpectedReturnShape,
                 millisecond_time_limit: None, input: Input) -> None:
        self.token = token
        self.description = description
        self.arguments = arguments
        self.expected_return_shape = expected_return_shape
        self.millisecond_time_limit = millisecond_time_limit
        self.input = input

    @staticmethod
    def from_dict(obj: Any) -> 'Part2Response':
        assert isinstance(obj, dict)
        token = from_str(obj.get("token"))
        description = from_str(obj.get("description"))
        arguments = Arguments.from_dict(obj.get("arguments"))
        expected_return_shape = ExpectedReturnShape.from_dict(obj.get("expected_return_shape"))
        millisecond_time_limit = (obj.get("millisecond_time_limit"))
        input = Input.from_dict(obj.get("input"))
        return Part2Response(token, description, arguments, expected_return_shape, millisecond_time_limit, input)

    def to_dict(self) -> dict:
        result: dict = {"token": from_str(self.token), "description": from_str(self.description),
                        "arguments": to_class(Arguments, self.arguments),
                        "expected_return_shape": to_class(ExpectedReturnShape, self.expected_return_shape),
                        "millisecond_time_limit": from_none(self.millisecond_time_limit),
                        "input": to_class(Input, self.input)}
        return result


def part2_response_from_dict(s: Any) -> Part2Response:
    return Part2Response.from_dict(s)


def part2_response_to_dict(x: Part2Response) -> Any:
    return to_class(Part2Response, x)
