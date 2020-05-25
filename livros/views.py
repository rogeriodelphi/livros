from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import LivroForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Livro


class EditoraListView(generic.ListView):
    model = Livro
    context_object_name = 'livros'
    template_name = 'livros/listar_livros.html'


class LivroCreateView(BSModalCreateView):
    template_name = 'livros/create_livro.html'
    form_class = LivroForm
    success_message = 'Sucesso: O Livro foi criado.'
    success_url = reverse_lazy('listar_livros')

class LivroUpdateView(BSModalUpdateView):
    model = Livro
    template_name = 'livros/update_livro.html'
    form_class = LivroForm
    success_message = 'Sucesso: O registro foi atualizado.'
    success_url = reverse_lazy('listar_livros')

class LivroReadView(BSModalReadView):
    model = Livro
    template_name = 'livros/read_livro.html'

class LivroDeleteView(BSModalDeleteView):
    model = Livro
    template_name = 'livros/delete_livro.html'
    success_message = 'Sucesso: O Livro foi removido.'
    success_url = reverse_lazy('listar_livros')




class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'livros/signup.html'
    success_message = 'A inscrição foi bem-sucedida. Agora você pode fazer login.'
    success_url = reverse_lazy('listar_livros')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'livros/login.html'
    success_message = 'Sucesso: você efetuou login com êxito.'
    success_url = reverse_lazy('listar_livros')



#listar livros
class LivroListView(generic.ListView):
    model = Livro
    context_object_name = 'livros'
    template_name = 'livros/listar_livros.html'