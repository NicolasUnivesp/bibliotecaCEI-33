# Generated by Django 4.1.6 on 2023-02-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=100)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('disponivel', models.BooleanField(blank=True, null=True)),
                ('notas', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
