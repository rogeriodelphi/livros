from django.urls import path
from . import views


urlpatterns = [
    path('listar_editoras', views.EditoraListView.as_view(), name='listar_editoras'),

    path('create_editora/', views.EditoraCreateView.as_view(), name='create_editora'),

    path('update_editora/<int:pk>', views.EditoraUpdateView.as_view(), name='update_editora'),

    path('read_editora/<int:pk>', views.EditoraReadView.as_view(), name='read_editora'),

    path('delete_editora/<int:pk>', views.EditoraDeleteView.as_view(), name='delete_editora'),
]