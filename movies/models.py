from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=150)
    year_of_release=models.PositiveIntegerField()
    category=models.CharField(max_length=150)
    director=models.CharField(max_length=150)
    image=models.ImageField(upload_to="pics",null=True)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.CharField(max_length=150, null=True)
    review_date = models.DateField(auto_now_add=True, null=True)

    class Meta:
        unique_together=('user','movie')