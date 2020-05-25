from django.urls import path
from . import views


urlpatterns = [
    path('listar_livros', views.LivroListView.as_view(), name='listar_livros'),

    path('create_livro/', views.LivroCreateView.as_view(), name='create_livro'),

    path('update_livro/<int:pk>', views.LivroUpdateView.as_view(), name='update_livro'),

    path('read_livro/<int:pk>', views.LivroReadView.as_view(), name='read_livro'),

    path('delete_livro/<int:pk>', views.LivroDeleteView.as_view(), name='delete_livro'),
]