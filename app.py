import logging
import time

from src.APIcontroller import APIcontroller
from src.ApiUtil import ApiUtil

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler('app_log.log'),
                        logging.StreamHandler()
                    ])

def problem(config, url):
    apiController = APIcontroller()

    start = time.time()
    apiController.from_url(url, token=config.api.token, test=False)
    end = (time.time() - start)

    if apiController.post_ok:
        logging.info(f" --> Successfully (in {end} seconds)")
    else:
        logging.error(f" --> Incorrect (in {end} seconds)")



if __name__ == '__main__':
    logging.info("Aplication start ----")
    config = ApiUtil.read_config()

    if ApiUtil.test_token(config.api.host, config.api.test_token, config.api.token):
        logging.info("Token validated")
    else:
        logging.error("Wrong token")


    logging.info("* Start assignments")
    
    logging.info("Assignments 1/2")
    problem(config, config.api.host + config.api.problem.part_1)

    logging.info("Assignments 2/2")
    problem(config, config.api.host + config.api.problem.part_2)

    logging.info("* All assignments terminated")

    logging.info("Aplication ended ----")
