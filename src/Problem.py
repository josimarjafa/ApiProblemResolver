import datetime
from typing import TypeVar, List

from src.data_model import Part1reply, Part2reply
from src.data_model.Part1Response import Leg, Part1Response
from src.data_model.Part1reply import Part1Reply
from src.data_model.Part2Response import Part2Response
from src.data_model.Part2reply import Part2Reply, Header

Response = TypeVar('Response', Part1Response, Part2Response)
Reply = TypeVar('Response', Part1Reply, Part2Reply)



class Problem:
    response: Response
    reply: Reply

    def __init__(self, response: Response) -> None:
        assert isinstance(response, (Part1Response, Part2Response))
        super().__init__()
        self.response = response

        if isinstance(self.response, Part1Response):
            self.reply = Part1Reply(Part1reply.Header(self.response.token), Part1reply.Data(self.leg_time()))
        else:
            self.reply = Part2Reply(Part2reply.Header(self.response.token), Part2reply.Data(self.return_legs()))


    def solution(self): return self.reply

    def return_legs(self):
        if isinstance(self.response, Part1Response):
            return []
        outbound_id = self.response.arguments.outbound_leg_id

        list_legs = []
        for fare in self.response.input.fares:
            if fare.legs[0] == outbound_id:
                list_legs.append(fare.legs[1])

        return list_legs

    def leg_time(self) -> datetime:
        if isinstance(self.response, Part2Response):
            return 0

        total = None
        fare_id = self.response.arguments.fare_id

        list_legs = []
        for fare in self.response.input.fares:
            if fare.id == fare_id:
                list_legs.append(fare.legs[0])
                list_legs.append(fare.legs[1])

        for leg in self.response.input.legs:
            if leg.id in list_legs:
                if total == None:
                    total = leg.arrival_utc.iso - leg.departure_utc.iso
                else:
                    total += leg.arrival_utc.iso - leg.departure_utc.iso

        return int(total.total_seconds())


    def __str__(self) -> str:
        return f"Flight #{self.response.input.legs[0].flight_number},  {self.response.input.legs[0].airline.name}\n" + self.__leg_to_str() \
               + f"\nTotal in seconds: {self.leg_time()} " \
                 f"\nRetrun legs: {self.return_legs()}"

    def __leg_to_str(self):
        result = ''
        for leg in self.response.input.legs:
            result += f"\t\t From: {leg.departure_airport.name} - {leg.departure_airport.state}\t ({leg.departure_utc.iso})\n" \
                      f"\t\t To:   {leg.arrival_airport.name} - {leg.arrival_airport.state}\t ({leg.arrival_utc.iso})\n"
        return result