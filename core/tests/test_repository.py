from django import test

from to_do import repository
from to_do.tests import model_factories


class TestRepository(test.TestCase):
    def setUp(self) -> None:
        self.project = model_factories.ProjectFactory(id=1)
        self.developers = model_factories.DeveloperFactory.create_batch(3)

        self.project.developers.set(self.developers)

    def test_get_developers_who_are_not_member_of_project(self):
        diff = repository.get_developers_who_are_not_member_of_project(1, [1, 2, 3, 4])

        self.assertEqual({3, 4}, diff)
