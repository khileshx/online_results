# Generated by Django 2.0.1 on 2018-09-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_auto_20180908_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectresult',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
