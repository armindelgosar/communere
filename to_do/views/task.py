from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.permissions import IsProductManager, IsProjectOwner, IsDeveloper, IsProjectMember
from core import repository as core_repository
from core.services import get_account
from to_do.serializers import task as task_serializer
from to_do.services.task_assignment import assign_task_to_developer
from django_filters import FilterSet
import django_filters


class TaskBaseViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return task_serializer.TaskListRetrieveSerializer
        return task_serializer.TaskCreateUpdateSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')

        return core_repository.get_project_tasks(project_id).prefetch_related(
            'assignees',
            'assignees__account',
        )


class TaskProductManagerViewSet(TaskBaseViewSet):
    permission_classes = [IsProductManager, IsProjectOwner]


class TaskDeveloperViewSet(TaskBaseViewSet):
    permission_classes = [IsDeveloper, IsProjectMember]

    def get_queryset(self):
        if self.action in ['get_assigned_tasks']:
            developer = get_account.get_developer(self.request.user)
            project_id = self.kwargs.get('project_id')

            return developer.tasks.filter(project_id=project_id)
        return super().get_queryset()

    def assign(self, *args, task_id, **kwargs):
        developer = get_account.get_developer(self.request.user)
        assign_task_to_developer(task_id, developer)

        return Response(status=status.HTTP_200_OK)

    def get_assigned_tasks(self, *args, **kwargs):
        return super().list(*args, **kwargs)
