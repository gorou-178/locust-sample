import logging

from locust.clients import HttpSession

from environments import REQUEST_TIMEOUT


def get(http_session: HttpSession, todo_id: int):
    with http_session.rename_request("/todos/{todo_id}"), \
            http_session.get(f"/todos/{todo_id}",
                             headers={"Content-Type": "application/json"},
                             timeout=REQUEST_TIMEOUT,
                             catch_response=True
                             ) as response:
        if 200 <= response.status_code < 300:
            response.success()
            return response.json()
        if response.status_code == 0:
            response.failure(f"timeout response: todo_id = {todo_id}")
        else:
            response.failure(f"error response: status_code = {response.status_code}")
        return None


def create(http_session: HttpSession, todo_id: int, title: str):
    params = {"id": todo_id, "title": title}
    with http_session.rename_request("/todos"), \
            http_session.post("/todos",
                              json=params,
                              headers={"Content-Type": "application/json"},
                              timeout=REQUEST_TIMEOUT,
                              catch_response=True
                              ) as response:
        if 200 <= response.status_code < 300:
            response.success()
            return response.json()
        if response.status_code == 0:
            response.failure(f"timeout response: todo_id = {todo_id}")
        else:
            response.failure(f"error response: status_code = {response.status_code}")
        return None
