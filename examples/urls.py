from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('listar_editora', views.EditoraListView.as_view(), name='listar_editora'),

    path('create/', views.BookCreateView.as_view(), name='create_book'),
    path('create_editora/', views.EditoraCreateView.as_view(), name='create_editora'),

    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),
    path('update_editora/<int:pk>', views.EditoraUpdateView.as_view(), name='update_editora'),

    path('read/<int:pk>', views.BookReadView.as_view(), name='read_book'),
    path('read_editora/<int:pk>', views.EditoraReadView.as_view(), name='read_editora'),

    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete_book'),
    path('delete_editora/<int:pk>', views.EditoraDeleteView.as_view(), name='delete_editora'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]