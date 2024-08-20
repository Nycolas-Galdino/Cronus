from app.core.scheduling import Scheduler
from datetime import datetime, timedelta


def test_add_task():
    scheduler = Scheduler()
    task = scheduler.add_task("Task 1", datetime.now() + timedelta(days=1))
    assert task["name"] == "Task 1"
    assert len(scheduler.tasks) == 1
