from django.db import models

# Create your models here.
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
    username=models.CharField(max_length=50,null=False,blank=False)
    password=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    verification=models.CharField(choices=verificationStatus,null=False,blank=False)