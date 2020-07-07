# Generated by Django 3.0.8 on 2020-07-07 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_nascimento', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
