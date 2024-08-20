from datetime import datetime


class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name: str, due_date: datetime):
        task = {"name": name, "due_date": due_date, "is_completed": False}
        self.tasks.append(task)
        return task

    def get_upcoming_tasks(self):
        return [task for task in self.tasks if task['due_date'] > datetime.now()]
