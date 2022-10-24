from core import repository as core_repository
from to_do import models


def assign_task_to_developer(task_id: int, developer: models.Developer):
    task = core_repository.get_task_by_id(task_id)
    task.assignees.add(developer)