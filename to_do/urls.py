from django.urls import path

from to_do.views.project import ProjectViewSet
from to_do.views.task import TaskProductManagerViewSet, TaskDeveloperViewSet

project_create_list_view = ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

project_update_retrieve_view = ProjectViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
})

task_manager_create_list_view = TaskProductManagerViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

task_manager_update_retrieve_view = TaskProductManagerViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
})

task_developer_create_list_view = TaskDeveloperViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


urlpatterns = [
    path('projects/', project_create_list_view),
    path('projects/<int:pk>/', project_update_retrieve_view),
    path('manager/<int:project_id>/tasks/', task_manager_create_list_view),
    path('manager/<int:project_id>/tasks/<int:pk>/', task_manager_update_retrieve_view),
    path('developer/<int:project_id>/tasks/', task_developer_create_list_view),
    path('developer/<int:project_id>/tasks/assigned/', TaskDeveloperViewSet.as_view({'get': 'get_assigned_tasks'})),
    path('developer/<int:project_id>/tasks/<int:task_id>/assign/', TaskDeveloperViewSet.as_view({'post': 'assign'})),
]
