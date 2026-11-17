import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".github" / "scripts"))

from todo import Task, TaskPool


def test_add_task():
    pool = TaskPool()
    task = Task("New Task")
    pool.add_task(task)
    assert len(pool.tasks) == 1


def test_get_open_tasks():
    pool = TaskPool()
    pool.populate()
    open_tasks = pool.get_open_tasks()
    assert len(open_tasks) == 3
    assert all(task.status == "ToDo" for task in open_tasks)


def test_get_done_tasks():
    pool = TaskPool()
    pool.populate()
    done_tasks = pool.get_done_tasks()
    assert len(done_tasks) == 3
    assert all(task.status == "Done" for task in done_tasks)
