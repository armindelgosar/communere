import factory

from core.tests.model_factory import BaseAccountFactory
from to_do import models


class DeveloperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Developer

    id = factory.Sequence(lambda n: n)
    account = factory.SubFactory(BaseAccountFactory)


class ProductManagerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductManager

    id = factory.Sequence(lambda n: n)
    account = factory.SubFactory(BaseAccountFactory)


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Project

    id = factory.Sequence(lambda n: n)
    project_name = 'test_project'
    product_manager = factory.SubFactory(ProductManagerFactory)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Task

    id = factory.Sequence(lambda n: n)
    title = 'test_task'
    project = factory.SubFactory(ProjectFactory)
