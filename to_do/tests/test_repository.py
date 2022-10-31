from django import test

from core import repository
from to_do.tests import model_factories


class TestRepository(test.TestCase):

    def test_get_developers_by_id(self):
        model_factories.DeveloperFactory.create_batch(3)

        result = repository.get_developers_by_id([0, 1, 2])
        self.assertEqual({0, 1, 2}, set(result.values_list('id', flat=True)))

    def test_get_product_manager_all_projects(self):
        manager = model_factories.ProductManagerFactory(id=2)
        model_factories.ProjectFactory(id=1, product_manager=manager)
        model_factories.ProjectFactory(id=2, product_manager=manager)

        self.assertEqual({1, 2}, set(repository.get_product_manager_all_projects(2).values_list('id', flat=True)))

    def test_get_task_by_id(self):
        model_factories.TaskFactory(id=1)
        self.assertEqual(1, repository.get_task_by_id(1).id)

    def test_get_project_tasks(self):
        proj = model_factories.ProjectFactory(id=1)

        model_factories.TaskFactory.create_batch(3, project=proj)

        self.assertEqual({0, 1, 2}, set(repository.get_project_tasks(1).values_list('id', flat=True)))

    def test_get_project_by_id(self):
        model_factories.ProjectFactory(id=1)

        self.assertEqual(1, repository.get_project_by_id(1).id)
