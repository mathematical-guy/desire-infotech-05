from rest_framework.views import APIView
from rest_framework.response import Response

from book_app.models import Book


class BookDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, id, format=None):
        book = Book.objects.first()
        data = {"title": book.title, "author": book.author}
        return Response(data)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     Book.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)