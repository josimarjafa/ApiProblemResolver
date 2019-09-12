import json

import requests
from requests import head

from src.ApiUtil import ApiUtil
from src.Problem import Problem, Response, Reply
from src.data_model.Part1Response import Part1Response
from src.data_model.Part1reply import Part1Reply
from src.data_model.Part2Response import Part2Response
from src.data_model.Part2reply import Part2Reply


class APIcontroller():
    problem: Problem
    url: str
    token: str

    def from_file(self, file: str) -> None:
        response_json = ApiUtil.read_from_file(file)
        self.load(response_json)

    def from_url(self, url: str, token: str, test=True, post=True) -> None:
        self.url = url
        self.token = token

        if test:
            r = requests.get(url=url, headers={"X-Lola-Homework-Access-Token":token},
                         params={'sample':test})
        else:
            r = requests.get(url=url, headers={"X-Lola-Homework-Access-Token": token})

        data = r.json()
        self.load(data)

        if post:
            self.__post()



    def __post(self) -> bool:
        r = requests.post(url=self.url, headers={"X-Lola-Homework-Access-Token": self.token},
                                                 json=self.solution().to_dict())
        self.post_status_code = r.status_code
        self.post_text = json.loads(r.text)
        self.post_ok = r.ok


    def solution(self) -> Part2Reply:
        return self.problem.reply

    def load(self, response_json):
        try:
            response_object = Part1Response.from_dict(response_json)
        except AssertionError:
            response_object = Part2Response.from_dict(response_json)
        self.problem = Problem(response_object)

    def __str__(self) -> str:
        return  f"\n{str(self.problem)}\n" \
               f"Response: {self.post_text}"









