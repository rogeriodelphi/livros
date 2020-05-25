from django.contrib import admin
from .models import Book

@admin.register(Book)
class ExamplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'author', 'price', 'pages', 'book_type', 'timestamp', 'editora')