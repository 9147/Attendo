# Generated by Django 4.2.6 on 2023-10-22 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_alter_class_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.student'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='prof',
        ),
        migrations.AddField(
            model_name='subject',
            name='prof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]