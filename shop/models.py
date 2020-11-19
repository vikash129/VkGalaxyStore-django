from django.db import models

# Create your models here.

class Product(models.Model):

    prod_id = models.AutoField
    prod_name = models.CharField(max_length=50)
    prod_price = models.IntegerField(default=0)
    catagery = models.CharField(max_length=50,default='')
    sub_category = models.CharField(max_length=50,default='')
    desc = models.CharField(max_length=200,default='')
    prod_date = models.DateField()
    prod_image = models.ImageField(upload_to='shop/images',default='')

    def __str__(self):
        return self.prod_name

    
