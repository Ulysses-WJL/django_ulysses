# Generated by Django 2.1.2 on 2018-11-01 13:25

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0009_auto_20181101_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]