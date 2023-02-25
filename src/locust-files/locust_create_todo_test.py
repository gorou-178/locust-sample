from locust import constant_throughput

from base_http_user import BaseHttpUser
from task_set import CreateTodo2TimesTaskSet


class CreateTodosTest(BaseHttpUser):
    tasks = {CreateTodo2TimesTaskSet}
    wait_time = constant_throughput(2)
