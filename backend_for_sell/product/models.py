from django.db import models

# Create your models here.
class category(models.Model):
    def __str__(self):
        return self.title
    title=models.CharField(max_length=50,blank=False,null=False)
    productsNumber=models.BigIntegerField(blank=False,null=False)
    creationDate=models.DateTimeField(blank=False,null=False)

class color(models.Model):
    def __str__(self):
        return self.color
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
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    discountPercentage=models.IntegerField(null=True,blank=True)
    status=models.CharField(choices=statuses,null=False)
    rate=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    creationDate=models.DateTimeField(blank=False,null=False)
    category=models.ForeignKey(category,on_delete=models.CASCADE)


    




