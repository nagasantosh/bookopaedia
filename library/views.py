from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Book, BookRequest
from .serializers import BookSerializer, BookRequestSerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    filterset_fields = ['category', 'author', 'age_group', 'is_available']
    search_fields = ['title', 'author', 'category', 'age_group', 'description']
    ordering_fields = ['title', 'author']

    # Optional: free-text query via `?q=`
    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        q = request.query_params.get('q')
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(author__icontains=q) | qs.filter(category__icontains=q)
        self.queryset = qs
        return super().list(request, *args, **kwargs)

class BookRequestViewSet(viewsets.ModelViewSet):
    queryset = BookRequest.objects.all().order_by('-timestamp')
    serializer_class = BookRequestSerializer
    http_method_names = ['post', 'get']  # admin can GET; public will POST

    # Public endpoint: allow anyone to submit
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

