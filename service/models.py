from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    # service app a images folder create hoye okhane image thakbe
    image = models.ImageField(upload_to="service/images/")
    
    def __str__(self):
        return self.name