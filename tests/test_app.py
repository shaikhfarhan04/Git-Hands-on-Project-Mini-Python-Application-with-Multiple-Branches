"""Starter tests. Expand these as you add features."""

from app import add_task, list_tasks, tasks


def test_tasks_list_starts_empty():
    tasks.clear()
    assert tasks == []
