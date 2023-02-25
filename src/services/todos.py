from locust.clients import HttpSession


def get(http_session: HttpSession, todo_id: int):
    http_session.request_name = "/todos/{todo_id}"
    http_session.get(f"/todos/{todo_id}",
                     headers={"Content-Type": "application/json"}
                     )
    http_session.request_name = None


def create(http_session: HttpSession, todo_id: int, title: str):
    params = {"id": todo_id, "title": title}
    http_session.request_name = "/todos"
    http_session.post("/todos", json=params, headers={"Content-Type": "application/json"})
    http_session.request_name = None
