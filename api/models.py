from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Books(models.Model):
    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=300)
    category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image',null=True)
    
    def __str__(self) :
        return self.name
    
    @property
    def avg_rating(self):
        rate=self.reviews_set.all().values_list('rating',flat=True)
        if rate:
            return sum(rate)/len(rate)
        else:
            return 0
        
    @property
    def review_count(self):
        count_review=self.reviews_set.count()
        if count_review:
            return count_review
        else:
            return 0

class Carts(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE) 
    date=models.DateTimeField(auto_now_add=True)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=255)

    def __str__(self) :
        return self.comment