from django.db import models

from core.models import BaseModel


class ProductManager(BaseModel):
    account = models.OneToOneField(
        to='core.BaseAccount',
        on_delete=models.CASCADE
    )
