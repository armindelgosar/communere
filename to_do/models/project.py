from django.db import models

from core.models import BaseModel


class Project(BaseModel):
    product_manager = models.ForeignKey(
        to='to_do.ProductManager',
        on_delete=models.CASCADE
    )

    project_name = models.CharField(
        max_length=32,
    )

    developers = models.ManyToManyField(
        to='to_do.Developer',
        related_name='projects'
    )
