from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


class BookAPIView(APIView):
    def get(self, request):
        book = Book.objects.all()
        return Response({'books': BookSerializer(book, many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'book': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Book.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = BookSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"book": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return  Response({"error:" "Method DELETE not allowed"})
        else:
            book = Book.objects.get(id=pk)
            book.delete()

        return Response({"book": "delete post " + str(pk)})
