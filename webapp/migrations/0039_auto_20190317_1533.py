# Generated by Django 2.1.5 on 2019-03-17 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0038_auto_20190308_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adapters',
            name='erro',
        ),
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
    ]
