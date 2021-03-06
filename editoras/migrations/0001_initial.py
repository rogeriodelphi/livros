# Generated by Django 2.1.11 on 2020-05-24 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cnpj', models.CharField(blank=True, max_length=14)),
                ('obs', models.TextField()),
            ],
            options={
                'verbose_name': 'Editora',
                'verbose_name_plural': 'Editoras',
                'db_table': 'Editora',
                'ordering': ['nome'],
                'managed': True,
            },
        ),
    ]
