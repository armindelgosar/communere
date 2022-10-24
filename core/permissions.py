from rest_framework import permissions

from core import repository, exceptions
from core.services import get_account


class IsDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            get_account.get_developer(request.user)
            return True
        except:
            return False


class IsProductManager(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            get_account.get_product_manager(request.user)
            return True
        except:
            return False


class IsProjectOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            manager = get_account.get_product_manager(request.user)
            project_id = view.kwargs.get('project_id')
            if repository.get_product_manager_project(manager_id=manager.id, id=project_id):
                return True
            raise exceptions.AccountIsNotProjectManagerError(
                f'Manager with ID: {manager.id} has not permission to project with ID: {project_id}')
        except:
            return False


class IsProjectMember(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            developer = get_account.get_developer(request.user)
            task_id = view.kwargs.get('task_id')
            task = repository.get_task_by_id(task_id=task_id)

            if task.project.developers.filter(id=developer.id).exists():
                return True
            raise exceptions.AccountIsNotProjectDeveloperError(
                f'Developer with ID: {developer.id} is not member of project with ID: {task.project_id}')
        except:
            return False
