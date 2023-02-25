from locust import constant

from base_http_user import BaseHttpUser
from task_set import CreateTodoScenario


class TodosTest(BaseHttpUser):
    tasks = {CreateTodoScenario}
    wait_time = constant(1)
