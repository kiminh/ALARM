# Generated by Django 2.1.5 on 2019-02-07 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_auto_20190207_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
        migrations.AlterField(
            model_name='recomendacaogerada',
            name='idClick',
            field=models.CharField(max_length=250),
        ),
    ]
