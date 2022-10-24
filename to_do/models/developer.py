from django.db import models

from core.models import BaseModel


class Developer(BaseModel):
    account = models.OneToOneField(
        to='core.BaseAccount',
        on_delete=models.CASCADE
    )
