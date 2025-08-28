from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    age_group = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='books/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='requests')
    yourname = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    flatNo = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.email}"


