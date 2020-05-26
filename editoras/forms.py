from bootstrap_modal_forms.forms import BSModalForm

from .models import Editora

class EditoraForm(BSModalForm):
    class Meta:
        model = Editora
        fields = ['nome', 'cnpj', 'obs']




