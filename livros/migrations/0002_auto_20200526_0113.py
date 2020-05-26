# Generated by Django 2.1.11 on 2020-05-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='livro',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=60),
        ),
    ]