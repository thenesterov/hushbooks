from django.shortcuts import render
from rest_framework import generics
from .models import Book, Publisher
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
