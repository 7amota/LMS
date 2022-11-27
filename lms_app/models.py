from django.db import models
class Category(models.Model):
 name = models.CharField(max_length=50)
 def __str__(self):
     return self.name
 

class Book(models.Model):
    #var
    choices = [
        ('availble','avalible'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    title = models.CharField(max_length = 150)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Photos/%y/%m/%d', null=True , blank=True)
    image_author = models.ImageField(upload_to='Photos/%y/%m/%d', null=True, blank=True)
    pages = models.IntegerField(null = True , blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2 , null = True , blank=True)
    rental_price = models.DecimalField(max_digits=5, decimal_places=2 , null = True , blank=True)
    rental_period = models.IntegerField(null = True , blank = True)
    rental_total = models.DecimalField(max_digits=6, decimal_places=3 , null = True , blank=True)
    active = models.BooleanField(default = True)
    status = models.CharField(max_length=50 , choices=choices, null = True , blank = True)
    category = models.ForeignKey(Category , on_delete=models.PROTECT , null = True , blank = True)
    #defs
    def __str__(self):
        return self.title
