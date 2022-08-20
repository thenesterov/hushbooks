from rest_framework import serializers

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'short_description', 'description', 'publisher_id')


