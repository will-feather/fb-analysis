# Generated by Django 4.1.3 on 2022-12-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballmatches',
            name='ambas_marcam',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='footballmatches',
            name='ftg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='footballmatches',
            name='htg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='footballmatches',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='footballmatches',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='footballmatches',
            name='ftag',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballmatches',
            name='fthg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballmatches',
            name='ftr',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='footballmatches',
            name='htag',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballmatches',
            name='hthg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballmatches',
            name='htr',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
