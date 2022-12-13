# Generated by Django 4.1.3 on 2022-12-08 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wall', '0002_realwreath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realwreath',
            name='orn1',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn2',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn3',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn4',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn5',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn6',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='orn7',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='realwreath',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='user_RealWreath', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
