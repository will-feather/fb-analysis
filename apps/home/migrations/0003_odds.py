# Generated by Django 4.1.3 on 2022-12-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0002_footballmatches_ambas_marcam_footballmatches_ftg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competicao', models.CharField(max_length=50)),
                ('evento', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=50)),
                ('mercado', models.CharField(max_length=50)),
                ('seleção', models.CharField(max_length=50)),
                ('a_favor', models.CharField(max_length=10)),
                ('contra', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'app_odds',
            },
        ),
    ]
