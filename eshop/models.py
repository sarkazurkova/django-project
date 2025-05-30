from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Autor(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno autora', help_text='Zadejte jméno autora',
                             error_messages={'blank': 'Jméno autora musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení autora', help_text='Zadejte příjmení autora',
                                error_messages={'blank': 'Příjmení autora musí být vyplněno'})
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    umrti = models.DateField(blank=True, null=True, verbose_name='Datum úmrtí')
    biografie = models.TextField(blank=True, verbose_name='Životopis')
    fotografie = models.ImageField(upload_to='autori', verbose_name='Fotografie', blank=True, null=True)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autoři'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Zanr(models.Model):
    nazev = models.CharField(max_length=20, verbose_name='Název žánru', help_text='Zadejte název žánru')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return f'{self.nazev}'


class Vydavatelstvi(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název vydavatelství', help_text='Zadejte název vydavatelství',
                             error_messages={'blank': 'Název vydavatelství je povinný údaj'})
    adresa = models.CharField(blank=True, null=True, max_length=200, verbose_name='Adresa')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Vydavatelství'
        verbose_name_plural = 'Vydavatelství'

    def __str__(self):
        return f'{self.nazev}'



class Druh(models.Model):
    druh = models.CharField(max_length=100, verbose_name='Literární druh', help_text='Zadejte název literárního žánru', 
                            error_messages={'blank': 'Nazev literárního druhu musí být vyplněn'})
    
    class Meta:
        ordering = ['druh']
        verbose_name = 'Literární druh'
        verbose_name_plural = 'Literární druhy'

    def __str__(self):
        return f'{self.druh}'


class Kniha(models.Model):
    titul = models.CharField(max_length=100, verbose_name='Titul knihy', help_text='Zadejte titul knihy',
                             error_messages={'blank': 'Titul knihy musí být vyplněn'})
    autori = models.ManyToManyField(Autor)
    obsah = models.TextField(blank=True, verbose_name='Obsah knihy', help_text='Vložte obsah knihy')
    pocet_stran = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999)],
                                              verbose_name='Počet stran', help_text='Zadejte počet stran (max. 9999)')
    rok_vydani = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1500), MaxValueValidator(2100)],
                                             verbose_name='Rok vydání', help_text='Zadejte rok vydání (1500 - 2100)')
    obalka = models.ImageField(upload_to='obalky', verbose_name='Obálka knihy')
    zanry = models.ManyToManyField(Zanr)
    druh = models.ForeignKey('Druh', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Literarní druh')
    vydavatelstvi = models.ForeignKey('Vydavatelstvi', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Vydavatelství')
    cena = models.PositiveIntegerField(verbose_name='Cena', help_text='Zadejte cenu knihy', error_messages={'blank':'Cena musí být vyplněna'})
    hodnoceni = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Hodnocení", blank=True, null=True, 
                                            help_text='Hodnocení knihy -> 1 = špatné, 5 = skvělé')


    class Meta:
        ordering = ['titul']
        verbose_name = 'Kniha'
        verbose_name_plural = 'Knihy'

    def __str__(self):
        return f'{self.titul} ({self.rok_vydani})'
    