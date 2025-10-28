from django.db import models

# Create your models here.
from django.db import models

class permission(models.Model):
    def __str__(self):
        return self.title
    
    methods=[
        ('GET','GET'),
        ('POST','POST'),
        ('PUT','PUT'),
        ('DELETE','DELETE')
    ]
    title=models.CharField(max_length=50,null=False,blank=False)
    apiLink=models.CharField(max_length=100,null=False,blank=False)
    method=models.CharField(max_length=100,null=False,blank=False,choices=methods)

class customer(models.Model):
    def __str__(self):
        return self.fullName
    
    verificationStatus=[
        ('Verified','Verified'),
        ('Not Verified','Not Verified')
    ]

    fullName=models.CharField(max_length=50,null=False,blank=False)
    birthDate=models.DateField(null=False,blank=False)
    Email=models.CharField(max_length=50,null=False,blank=False)
    customername=models.CharField(max_length=50,null=False,blank=False)
    password=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    verification=models.CharField(choices=verificationStatus,null=False,blank=False)
    permission=models.ManyToManyField(permission,null=False)
