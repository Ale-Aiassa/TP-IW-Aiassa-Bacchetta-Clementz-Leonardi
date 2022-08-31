# Generated by Django 4.1 on 2022-08-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='juego',
            options={'ordering': ['id'], 'verbose_name': 'Juegos', 'verbose_name_plural': 'Juegos'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['id'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='Correo Obligatorio', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='Password obligatorio', max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='Username obligatorio', max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='Apellido obligatorio', max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='Nombre obligatorio', max_length=20, unique=True),
        ),
        migrations.AlterModelTable(
            name='juego',
            table='Juego',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='Usuario',
        ),
    ]