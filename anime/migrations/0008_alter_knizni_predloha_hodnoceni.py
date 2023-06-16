# Generated by Django 4.2 on 2023-05-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_alter_knizni_predloha_hodnoceni_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knizni_predloha',
            name='hodnoceni',
            field=models.CharField(choices=[(1, 'VERY BAD'), (2, 'BAD'), (3, 'AVERAGE'), (4, 'GOOD'), (5, 'VERY GOOD')], default='1', help_text='Zadej hodnocení', max_length=1, verbose_name='Hodnocení'),
        ),
    ]
