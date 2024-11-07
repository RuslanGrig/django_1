from django.db import models

class Phone(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=200, null=False) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    image = models.URLField(max_length=200) 
    release_date = models.DateField() 
    lte_exists = models.BooleanField() 
    slug = models.SlugField(unique=True, blank=True) 
 
    def __str__(self): 
        return self.name
