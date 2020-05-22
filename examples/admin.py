from django.contrib import admin
from .models import Book
from .models import Editora

@admin.register(Book)
class ExamplesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'author', 'price', 'pages', 'book_type', 'timestamp', 'editora')


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj')
    list_display_links = ('nome',)