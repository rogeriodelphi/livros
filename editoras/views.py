from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import EditoraForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Editora


class EditoraListView(generic.ListView):
    model = Editora
    context_object_name = 'editoras'
    template_name = 'editoras/listar_editoras.html'

#Criar uma nova Editora
class EditoraCreateView(BSModalCreateView):
    template_name = 'editoras/create_editora.html'
    form_class = EditoraForm
    success_message = 'Sucesso: A Editora foi criada.'
    success_url = reverse_lazy('listar_editoras')

#Ver dados de uma Editora
class EditoraReadView(BSModalReadView):
    model = Editora
    template_name = 'editoras/read_editora.html'

#Atualizar dados de uma Editora
class EditoraUpdateView(BSModalUpdateView):
    model = Editora
    template_name = 'editoras/update_editora.html'
    form_class = EditoraForm
    success_message = 'Sucesso: O registro foi atualizado.'
    success_url = reverse_lazy('listar_editoras')


#Excluir dados de uma Editora
class EditoraDeleteView(BSModalDeleteView):
    model = Editora
    template_name = 'editoras/delete_editora.html'
    success_message = 'Sucesso: A Editora foi removida.'
    success_url = reverse_lazy('listar_editoras')