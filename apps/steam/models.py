from django.db import models

# Create your models here.
class Resultados(models.Model):
    name = models.CharField(max_length=50)
    skin= models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    pattern = models.CharField(max_length=50)
    link_buy = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'resultado'
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'

class SearchItems(models.Model):
    name_weapon_skin = models.CharField(max_length=50)
    
    def __str__(self):
        return "%s"%self.name_weapon_skin
    class Meta:
        db_table = 'search_items'
        verbose_name = 'Search Item'
        verbose_name_plural = 'Search Items'

class SearchItemExteriores(models.Model):
    exterior = models.CharField(max_length=50)
    
    def __str__(self):
        return "({})".format(self.exterior)

    class Meta:
        db_table = 'search_items_exterioress'
        verbose_name = 'Search Item Exterior'
        verbose_name_plural = 'Search Items Exteriores'

class Exteriores(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return "(%s)"%self.name
        
    class Meta:
        db_table = 'exteriores'
        verbose_name = 'Exterior'
        verbose_name_plural = 'Exteriores'

class Armas(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return "%s"%self.name
        
    class Meta:
        db_table = 'armas'
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'