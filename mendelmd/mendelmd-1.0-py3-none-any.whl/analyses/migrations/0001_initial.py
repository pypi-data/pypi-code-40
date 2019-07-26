# Generated by Django 2.1.4 on 2018-12-27 08:50

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '__first__'),
        ('projects', '0001_initial'),
        ('files', '0001_initial'),
        ('mapps', '__first__'),
        ('samples', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('status', models.TextField(blank=True, null=True)),
                ('apps', models.ManyToManyField(to='mapps.App')),
                ('files', models.ManyToManyField(to='files.File')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('samples', models.ManyToManyField(to='samples.Sample')),
                ('tasks', models.ManyToManyField(to='tasks.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'analyses',
            },
        ),
        migrations.CreateModel(
            name='AnalysisType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('repository', models.CharField(blank=True, max_length=600, null=True)),
            ],
            options={
                'verbose_name_plural': 'analysis_types',
            },
        ),
    ]
