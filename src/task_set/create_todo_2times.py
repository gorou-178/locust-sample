import random

from locust import SequentialTaskSet, task

from services import todos


class CreateTodo2TimesTaskSet(SequentialTaskSet):

    def create_todo(self):
        todos.create(self.client,
                     random.randint(1, 1000),
                     self.user.test_data)

    def get_todo(self):
        todos.get(self.client, random.randint(1, 1000))

    tasks = [
        create_todo,
        get_todo,
        create_todo,
        get_todo
    ]

    @task
    def stop(self):
        self.interrupt()
