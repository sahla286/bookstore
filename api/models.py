from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=300)
    category=models.CharField(max_length=100)
    image=models.ImageField(null=True)
    
    # building render method
    # __str__ string representation method
    def __str__(self) :
        return self.name