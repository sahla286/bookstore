from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Books(models.Model):
    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=300)
    category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=True)
    
    # building render method
    # __str__ string representation method
    def __str__(self) :
        return self.name

class Carts(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)