from rest_framework.viewsets import ModelViewSet
from core.permissions import IsProductManager, IsProjectOwner, IsDeveloper, IsProjectMember
from core import repository as core_repository
from core.services.get_account import get_product_manager, get_developer
from to_do.serializers import task as task_serializer
from to_do.services.task_assignment import assign_task_to_developer


class TaskBaseViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return task_serializer.TaskListRetrieveSerializer
        return task_serializer.TaskCreateUpdateSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')

        return core_repository.get_project_tasks(project_id).select_related(
            'assignees',
            'assignees__account',
        )


class TaskProductManagerViewSet(TaskBaseViewSet):
    permission_classes = [IsProductManager, IsProjectOwner]


class TaskDeveloperViewSet(TaskBaseViewSet):
    permission_classes = [IsDeveloper, IsProjectMember]

    def assign(self, *args, task_id, **kwargs):
        developer = get_developer(self.request.user)
        assign_task_to_developer(task_id, developer)
