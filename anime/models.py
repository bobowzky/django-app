from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class Ilustrator(models.Model):
    jmeno = models.CharField(max_length=20, verbose_name='Jméno ilustrátora', help_text = 'Zadej jméno ilustrátora')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení ilustrátora',
                                help_text = 'Zadej příjmení ilustrátora', null=True)
    zivotopis = models.TextField(blank=True, null=True)
    datum_narozeni = models.DateField(verbose_name='Datum narození ilustrátora', null=True, blank=True)

    class Meta:
        verbose_name = 'Ilustrátor'
        ordering = ['prijmeni']
        verbose_name_plural = 'Ilustrátoři'

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'


class Autor(models.Model):
    jmeno = models.CharField(max_length=20, verbose_name='Jméno autora', help_text='Zadej jméno autora')
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení autora',
                                    help_text='Zadej příjmení autora', null=True)
    zivotopis = models.TextField(blank=True, null=True)
    datum_narozeni = models.DateField(verbose_name='Datum narození autora', null=True, blank=True)
    foto = models.ImageField(upload_to='autori', null=True, blank=True, verbose_name='Fotka autora', help_text='Nahrejte fotku autora' )

    class Meta:
        verbose_name = 'Autor'
        ordering = ['prijmeni']
        verbose_name_plural = 'Autoři'

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'


class Knizni_predloha(models.Model):

    HODNOCENI = [
        ("1", "VERY BAD"),
        ("2","BAD"),
        ("3","AVERAGE"),
        ("4", "GOOD"),
        ("5", "VERY GOOD"),
    ]
    titul = models.CharField(max_length=100, verbose_name='Název', help_text='Zadej název knižní předlohy')
    rok_vydani = models.IntegerField(verbose_name='Rok vydání', help_text='Zadej rok vydání knižní předlohy')
    pocet_stran = models.IntegerField(verbose_name='Počet stran', help_text='Zadej počet stran')
    hodnoceni = models.CharField(max_length=1, default='1', choices=HODNOCENI, verbose_name='Hodnocení', help_text='Zadej hodnocení' )
    obalka = models.ImageField(upload_to='knizni_predlohy', null=True, blank=True, verbose_name='Obálka knižní předlohy',
                             help_text='Nahrejte obálku')
    class Meta:
        verbose_name = 'Knižní předloha'
        verbose_name_plural = 'Knižní předlohy'
        ordering = ['titul']

    def __str__(self):
        return self.titul

class Anime(models.Model):
    ZANRY = [
        ("fantasy", "Fantasy"),
        ("romance", "Romance"),
        ("sci-fi", "Sci-Fi"),
        ("adventure", "Adventure"),
        ("mecha", "Mecha")
    ]
    HODNOCENI_ANIME = [
        ("1", "VERY BAD"),
        ("2","BAD"),
        ("3","AVERAGE"),
        ("4", "GOOD"),
        ("5", "VERY GOOD"),
    ]
    titul = models.CharField(max_length=100, verbose_name='Název', help_text='Zadej název anime')
    zanr = models.CharField(max_length=20, default='fantasy', choices=ZANRY, verbose_name='Žánr', help_text='Zadej žánr')
    rok_vydani = models.IntegerField(verbose_name='Rok vydání', help_text='Zadej rok vydání knižní předlohy')
    hodnoceni = models.CharField(max_length=1, default='1', choices=HODNOCENI_ANIME, verbose_name='Hodnocení', help_text='Zadej hodnocení' )
    studio = models.CharField(max_length=50, verbose_name='Studio', help_text='Zadej název studia')
    ilustracni_foto = models.ImageField(upload_to='ilustracni_foto', null=True, blank=True, verbose_name='Ilustrační foto',
                             help_text='Nahrejte ilustrační foto')
    obsah = models.TextField(blank=True, verbose_name='Obsah knihy', help_text='Vložte obsah knihy')

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        ordering = ['titul']

    def __str__(self):
        return self.titul