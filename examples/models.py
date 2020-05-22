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



class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Capa Dura'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    editora = models.ForeignKey(Editora, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'Book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']





