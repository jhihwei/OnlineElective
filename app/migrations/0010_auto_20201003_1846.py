# Generated by Django 3.1.2 on 2020-10-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201003_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course_record',
            options={'ordering': ('student',), 'verbose_name_plural': '選課記錄'},
        ),
        migrations.AddField(
            model_name='course_record',
            name='allocation',
            field=models.BooleanField(default=False, verbose_name='已分配'),
        ),
    ]
