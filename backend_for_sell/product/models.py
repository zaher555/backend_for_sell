from django.db import models
from customer.models import customer
# Create your models here.
class category(models.Model):
    def __str__(self):
        return self.title
    title=models.CharField(max_length=50,blank=False,null=False)
    productsNumber=models.BigIntegerField(blank=True,null=True)

class color(models.Model):
    def __str__(self):
        return self.colorName
    colorName=models.CharField(max_length=50,blank=False,null=False)

class product(models.Model):
    def __str__(self):
        return self.title

    statuses=[
        ('Available','Available'),
        ('Not Available','Not Available')
    ]
    title=models.CharField(max_length=50,blank=False,null=False)
    description=models.CharField(max_length=500,blank=False,null=False)
    price=models.DecimalField(max_digits=5,decimal_places=2,blank=False,null=False)
    color=models.ManyToManyField(color,blank=False,null=False)
    image=models.ImageField(upload_to='photos/%y/%m/%d',null=True)
    discountPercentage=models.IntegerField(null=True,blank=True)
    status=models.CharField(choices=statuses,null=False)
    rate=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE,related_name='products')

class customer_rate(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    rate=models.FloatField(null=False,blank=False)
    class Meta:
        unique_together = ('customer', 'product')


    




