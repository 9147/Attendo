# Generated by Django 4.2.6 on 2023-10-23 11:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0008_alter_subject_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prof',
            field=models.ManyToManyField(blank=True, null=True, related_name='profs', to=settings.AUTH_USER_MODEL),
        ),
    ]