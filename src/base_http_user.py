from locust import events, HttpUser
from locust.runners import MasterRunner
import logging


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        logging.info("test start(worker)")
    else:
        logging.info("test start(master)")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        logging.info("test stop(worker)")
    else:
        logging.info("test stop(master)")


@events.request.add_listener
def logging_response(request_type, name, response_time, response_length, response,
                     context, exception, start_time, url, **kwargs):
    if exception:
        logging.info(f"request:{name} failed -> {exception}")
    else:
        logging.info(f"request:{name} OK -> time: {round(response_time, 3)}, size: {response_length}")


class BaseHttpUser(HttpUser):
    abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = "test_data"
