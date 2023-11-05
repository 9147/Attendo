# Generated by Django 4.2.6 on 2023-11-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('lid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('student', models.ManyToManyField(blank=True, to='mainapp.student')),
                ('subjects', models.ManyToManyField(blank=True, to='mainapp.subject')),
            ],
        ),
    ]