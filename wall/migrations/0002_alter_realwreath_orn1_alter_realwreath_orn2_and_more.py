# Generated by Django 4.1.3 on 2022-12-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realwreath',
            name='orn1',
            field=models.CharField(default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn2',
            field=models.CharField(default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn3',
            field=models.CharField(default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn4',
            field=models.CharField(default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn5',
            field=models.CharField(default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn6',
            field=models.CharField(default=-1, max_length=200),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn7',
            field=models.CharField(default=-1, max_length=200),
        ),
    ]