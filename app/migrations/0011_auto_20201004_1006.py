# Generated by Django 3.1.2 on 2020-10-04 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201003_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_record',
            name='course',
            field=models.ForeignKey(db_column='name_code', on_delete=django.db.models.deletion.PROTECT, to='app.course', verbose_name='課程'),
        ),
    ]