import factory

from core import models


class BaseAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BaseAccount

    id = factory.Sequence(lambda n: n)
    username = factory.Sequence(lambda n: f'test_username{n}')
    gender = 'male'
    first_name = 'test_first_name'
    last_name = 'test_last_name'
    email = factory.Sequence(lambda n: f'test{n}@gmail.com')
