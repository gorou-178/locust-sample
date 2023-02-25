import random

from locust import SequentialTaskSet, task

from services import todos


class CreateTodoScenario(SequentialTaskSet):
    @task
    def create_todo(self):
        todos.create(self.client,
                     random.randint(1, 1000),
                     self.user.test_data)

    @task
    def get_todo(self):
        todos.get(self.client, random.randint(1, 1000))

    @task
    def stop(self):
        self.interrupt()
