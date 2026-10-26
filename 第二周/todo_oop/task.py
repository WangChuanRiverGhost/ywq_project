class Task:
    def __init__(self, title, status="todo", task_id=None):
        self.id = task_id
        self.title = title
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.title} ({self.status})"