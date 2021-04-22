# Generated by Django 3.2 on 2021-04-19 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('preco', models.IntegerField()),
                ('quantidade', models.IntegerField()),
                ('status', models.CharField(choices=[('Abastecer', 'Esta item esta acabando'), ('Disponivel', 'Este item esta disponivel'), ('Indisponivel', 'Este item acabou')], default='Indisponivel', max_length=20)),
            ],
        ),
    ]
