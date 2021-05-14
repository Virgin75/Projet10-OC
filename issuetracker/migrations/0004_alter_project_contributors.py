# Generated by Django 3.2.2 on 2021-05-14 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issuetracker', '0003_auto_20210514_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(through='issuetracker.Contributor', to=settings.AUTH_USER_MODEL),
        ),
    ]