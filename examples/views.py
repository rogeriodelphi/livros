from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import BookForm, EditoraForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Book, Editora

class Index(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'

#Listar Editoras
class EditoraListView(generic.ListView):
    model = Editora
    context_object_name = 'editoras'
    template_name = 'examples/listar_editoras.html'


class BookCreateView(BSModalCreateView):
    template_name = 'examples/create_book.html'
    form_class = BookForm
    success_message = 'Sucesso: O Livro foi criado.'
    success_url = reverse_lazy('index')

#Criar Editora
class EditoraCreateView(BSModalCreateView):
    template_name = 'examples/create_editora.html'
    form_class = EditoraForm
    success_message = 'Sucesso: A Editora foi criada.'
    success_url = reverse_lazy('listar_editora')



class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'examples/update_book.html'
    form_class = BookForm
    success_message = 'Sucesso: O registro foi atualizado.'
    success_url = reverse_lazy('index')

#Atualizar Editora
class EditoraUpdateView(BSModalUpdateView):
    model = Editora
    template_name = 'examples/update_editora.html'
    form_class = EditoraForm
    success_message = 'Sucesso: O registro foi atualizado.'
    success_url = reverse_lazy('listar_editora')




class BookReadView(BSModalReadView):
    model = Book
    template_name = 'examples/read_book.html'

class EditoraReadView(BSModalReadView):
    model = Editora
    template_name = 'examples/read_editora.html'




class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'examples/delete_book.html'
    success_message = 'Sucesso: O Livro foi removido.'
    success_url = reverse_lazy('index')

#Excluir Editora
class EditoraDeleteView(BSModalDeleteView):
    model = Editora
    template_name = 'examples/delete_editora.html'
    success_message = 'Sucesso: A Editora foi removida.'
    success_url = reverse_lazy('listar_editora')






class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'examples/signup.html'
    success_message = 'A inscrição foi bem-sucedida. Agora você pode fazer login.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'examples/login.html'
    success_message = 'Sucesso: você efetuou login com êxito.'
    success_url = reverse_lazy('index')


