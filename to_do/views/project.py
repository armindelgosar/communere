from rest_framework.viewsets import ModelViewSet

from core.permissions import IsProductManager
from core import repository as core_repository
from core.services.get_account import get_product_manager
from to_do.serializers import project as project_serializer


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsProductManager]

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update']:
            return project_serializer.ProjectCreateUpdateSerializer
        return project_serializer.ProjectListRetrieveSerializer

    def get_queryset(self):
        project_manager = get_product_manager(self.request.user)
        return core_repository.get_product_manager_all_projects(project_manager.id).select_related(
            'developers',
            'developers__account',
        )
