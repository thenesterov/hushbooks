import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Book


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    short_description = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=1000)
    publisher_id = serializers.IntegerField()
    year = serializers.IntegerField()
    part = serializers.IntegerField()
    page_count = serializers.IntegerField()
    table_of_content = serializers.JSONField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.short_description = validated_data.get("short_description", instance.short_description)
        instance.description = validated_data.get("description", instance.description)
        instance.publisher_id = validated_data.get("publisher_id", instance.publisher_id)
        instance.page_count = validated_data.get("page_count", instance.page_count)
        instance.part = validated_data.get("part", instance.part)
        instance.year = validated_data.get("year", instance.year)
        instance.table_of_content = validated_data.get("table_of_content", instance.table_of_content)
        instance.save()
        return instance
