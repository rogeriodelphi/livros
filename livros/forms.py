from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Livro


class LivroForm(BSModalForm):
    data_publicacao = forms.DateField(
        error_messages={'inválida': 'Digite um formato válido para a data, conforme exemplo: DD/MM/AAAA.'}
    )

    class Meta:
        model = Livro
        exclude = ['data_lancamento']















class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
