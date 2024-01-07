from django.db import models

# Create your models here.


class Languages(models.Model):
    name = models.CharField('Lenguaje',max_length=20)

    class Meta:
        verbose_name = ('Lenguaje')
        verbose_name_plural = ('Lenguajes')

    def __str__(self):
        return self.name
    
class Countries (models.Model):
    country = models.CharField('Pais', max_length=50)
    flag = models.ImageField(upload_to='banderas/')
    
    class Meta:
        verbose_name = ('Pais')
        verbose_name = ('Paises')

    def __str__(self):
        return self.country

class Floor(models.Model):
    name = models.CharField('Piso' ,max_length=20)
    description = models.CharField('Descripcion', max_length=250)

    class Meta:
        verbose_name = ('Piso')
        verbose_name = ('Pisos')

    def __str__(self):
        return self.name
    

class Museum(models.Model):
    name = models.CharField('Museo', max_length=50)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    language = models.ManyToManyField(Languages)
    floor = models.ManyToManyField(Floor) 
    image = models.ImageField(upload_to='museos/')

    class Meta:
        verbose_name = ('Museo') 
        verbose_name_plural = ('Museos')

    def __str__(self):
        return self.name   