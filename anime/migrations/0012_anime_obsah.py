# Generated by Django 4.2 on 2023-06-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0011_alter_knizni_predloha_hodnoceni'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='obsah',
            field=models.TextField(blank=True, help_text='Vložte obsah knihy', verbose_name='Obsah knihy'),
        ),
    ]
