import logging
import random

from locust import SequentialTaskSet, task

from services import todos


class CreateTodoScenario(SequentialTaskSet):
    @task
    def create_todo(self):
        response = todos.create(self.client,
                                random.randint(1, 1000),
                                self.user.test_data)
        logging.info(response)

    @task
    def get_todo(self):
        response = todos.get(self.client, random.randint(1, 1000))
        logging.info(response)

    @task
    def stop(self):
        self.interrupt()
