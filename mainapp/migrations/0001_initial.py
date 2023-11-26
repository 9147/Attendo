# Generated by Django 4.2.6 on 2023-11-19 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('cid', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('Class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.class')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('sid', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('partial', models.BooleanField(default=False)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.class')),
                ('prof', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, to='mainapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_classList', models.BooleanField(default=True)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.class')),
                ('student', models.ManyToManyField(blank=True, to='mainapp.student')),
                ('subjects', models.ManyToManyField(blank=True, to='mainapp.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('classno', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('N', 'Not applicable')], max_length=10)),
                ('rollno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.student')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subject')),
            ],
        ),
    ]
