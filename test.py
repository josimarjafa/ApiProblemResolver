import unittest

import src.ApiUtil
import src.data_model.Config as Config
import app
from src.APIcontroller import APIcontroller
from src.ApiUtil import ApiUtil
from src.Problem import Problem
from src.data_model.Part1reply import Part1Reply
from src.data_model.Part1Response import Part1Response
from src.data_model.Part2Response import Part2Response
from src.data_model.Part2reply import Part2Reply


class A_Configuration(unittest.TestCase):
    def setUp(self):
        self.config = ApiUtil.read_config()

    def test_Config_file(self):
        cfg = ApiUtil.read_from_file("config.yml")

        result = Config.config_from_dict(cfg)

        self.assertEqual(self.config.to_dict(), result.to_dict(), "Should be equal")


    def test_token(self):
        result = ApiUtil.test_token(self.config.api.host, self.config.api.test_token, self.config.api.token)

        self.assertTrue(result, "Not valid token")

class B_Mock_Assesments(unittest.TestCase):

    def setUp(self):
        self.config = ApiUtil.read_config()


    def test_load_from_file(self):
        apiController = APIcontroller()
        apiController.from_file("part_1_response.json")

        apiController2 = APIcontroller()
        apiController2.from_file("part_2_response.json")

        part1reply_json = ApiUtil.read_from_file("part_1_reply.json")
        part1reply_object = Part1Reply.from_dict(part1reply_json)

        part2reply_json = ApiUtil.read_from_file("part_2_reply.json")
        part2reply_object = Part2Reply.from_dict(part2reply_json)

        self.assertEqual(apiController.solution().to_dict(), part1reply_object.to_dict())
        self.assertEqual(apiController2.solution().to_dict(), part2reply_object.to_dict())


    def test_load_from_url(self):
        apiController = APIcontroller()
        apiController.from_url(self.config.api.host + self.config.api.problem.part_1,
                               token=self.config.api.token)

        self.assertIsNotNone(apiController.solution().data.total_seconds)

        apiController.from_url(self.config.api.host + self.config.api.problem.part_2,
                               token=self.config.api.token)

        self.assertIsNotNone(apiController.solution().data.return_leg_ids)

class C_full_test(unittest.TestCase):
    def setUp(self):
        self.config = ApiUtil.read_config()


    def test_problem_1(self):
        apiController = APIcontroller()
        apiController.from_url(self.config.api.host + self.config.api.problem.part_1,
                               token=self.config.api.token, test=False)

        self.assertTrue(apiController.post_ok, apiController)
        self.assertTrue(apiController.post_text['correct'], apiController)

    def test_problem_2(self):
        apiController = APIcontroller()
        apiController.from_url(self.config.api.host + self.config.api.problem.part_2,
                               token=self.config.api.token, test=False)

        self.assertTrue(apiController.post_ok, apiController)
        self.assertTrue(apiController.post_text['correct'], apiController)



if __name__ == '__main__':
    unittest.main()