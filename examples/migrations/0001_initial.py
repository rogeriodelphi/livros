# Generated by Django 2.1.11 on 2020-05-24 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('editoras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField(null=True)),
                ('author', models.CharField(blank=True, max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('book_type', models.PositiveSmallIntegerField(choices=[(1, 'Capa Dura'), (2, 'Paperback'), (3, 'E-book')])),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='editoras.Editora')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'Book',
                'ordering': ['title'],
                'managed': True,
            },
        ),
    ]
