from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

class BookAPIView(APIView):
    def get(self, request):
        book = Book.objects.all()
        return Response({'posts': BookSerializer(many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    '''
    def put(self, requset, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Book.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = BookSerializer(data=requset.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return  Response({"error:" "Method DELETE not allowed"})



        return Response({"post": "delete post " + str(pk)})
    '''