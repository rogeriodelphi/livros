from django.db import models
from editoras .models import Editora

class Livro(models.Model):
    capa_dura = 1
    livro_bolso = 2
    e_book = 3
    e_pub = 4
    TIPOS_LIVROS = (
        (capa_dura, 'Capa Dura'),
        (livro_bolso, 'Livro de Bolso'),
        (e_book, 'E-book'),
        (e_pub, 'E-Pub'),
    )
    titulo = models.CharField(max_length=60)
    data_publicacao = models.DateField(null=True)
    autor = models.CharField(max_length=30, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    paginas = models.IntegerField(blank=True, null=True)
    tipo_livro = models.PositiveSmallIntegerField(choices=TIPOS_LIVROS)
    isbn = models.CharField(max_length=17)

    data_lancamento = models.DateField(auto_now_add=True, auto_now=False)
    editora = models.ForeignKey(Editora, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'Livro'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']





