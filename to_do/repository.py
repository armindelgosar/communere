from core import repository as core_repository


def get_developers_who_are_not_member_of_project(project_id: int, developer_ids: list):
    project = core_repository.get_project_by_id(project_id)
    if project:
        return set(developer_ids).difference(set(project.developers.all().values_list('id', flat=True)))
