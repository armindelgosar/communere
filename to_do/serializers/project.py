from django.db import transaction
from rest_framework import serializers

from core import repository as core_repository
from to_do.models import Project


class ProjectCreateUpdateSerializer(serializers.ModelSerializer):
    developer_ids = serializers.ListSerializer(write_only=True, child=serializers.IntegerField())

    class Meta:
        model = Project
        fields = (
            'project_name',
            'developer_ids',
            'product_manager',
        )

    def create(self, validated_data):
        with transaction.atomic():
            developer_ids = validated_data.pop('developer_ids', [])
            developers = core_repository.get_developers_by_id(developer_ids)

            project = super().create(validated_data)

            project.developers.set(developers)

            return project

    def update(self, instance, validated_data):
        with transaction.atomic():
            developer_ids = validated_data.pop('developer_ids', [])
            developers = core_repository.get_developers_by_id(developer_ids)

            project = super().update(instance, validated_data)

            project.developers.set(developers)

            return project


class ProjectListRetrieveSerializer(serializers.ModelSerializer):
    developers = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            'id',
            'project_name',
            'developers',
        )
        read_only_fields = (
            'id',
            'project_name',
            'developers',
        )

    def get_developers(self, project):
        return project.developers.all().values_list('account__first_name', flat=True)
