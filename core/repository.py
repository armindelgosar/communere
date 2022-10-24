from to_do import models


def get_developers_by_id(ids: list):
    return models.Developer.active_objects.filter(id__in=ids)


def get_product_manager_all_projects(manager_id: int, **kwargs):
    return models.Project.active_objects.filter(product_manager_id=manager_id, **kwargs)


def get_product_manager_project(manager_id: int, **kwargs):
    return models.Project.active_objects.filter(product_manager_id=manager_id, **kwargs).last()


def get_task_by_id(task_id: int, **kwargs):
    return models.Task.active_objects.filter(id=task_id, **kwargs).last()


def get_project_tasks(project_id: int):
    return models.Task.active_objects.filter(project_id=project_id)


def get_project_by_id(project_id: int):
    return models.Project.active_objects.filter(id=project_id).last()
