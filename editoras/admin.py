from django.contrib import admin
from .models import Editora

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj')
    list_display_links = ('nome',)