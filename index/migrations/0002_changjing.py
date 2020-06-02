# Generated by Django 2.2.12 on 2020-06-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='changjing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('index', models.IntegerField(max_length=3)),
            ],
            options={
                'verbose_name': '场景',
                'verbose_name_plural': '场景',
                'ordering': ['index'],
            },
        ),
    ]
