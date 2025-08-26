from rest_framework import serializers
from .models import Book, BookRequest

class BookSerializer(serializers.ModelSerializer):
    image_src = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'age_group', 'description', 'is_available', 'image_src']

    def get_image_src(self, obj):
        request = self.context.get('request')
        if obj.image:
            url = obj.image.url
            return request.build_absolute_uri(url) if request else url
        return obj.image_url or ''

class BookRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRequest
        fields = ['id', 'book', 'email', 'mobile', 'timestamp']
        read_only_fields = ['timestamp']
