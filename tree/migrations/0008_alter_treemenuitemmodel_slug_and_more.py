# Generated by Django 4.2.7 on 2023-11-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0007_alter_treemenuitemmodel_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treemenuitemmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, verbose_name='Item slug'),
        ),
        migrations.AlterField(
            model_name='treemenuitemmodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Item title'),
        ),
        migrations.AlterField(
            model_name='treemenumodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, verbose_name='Menu slug'),
        ),
    ]