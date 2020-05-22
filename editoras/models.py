from django.db import models


class Editora (models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, blank=True)
    obs = models.TextField()

    class Meta:
        managed = True
        db_table = 'Editora'
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['nome']

    def __str__(self):
        return self.nome
