from django.db import models # type: ignore

# Create your models here.
class contact_information(models.Model):
    username=models.CharField(max_length=10, blank=False)
    email=models.CharField(max_length=20, blank=False)
    number=models.CharField( max_length=11)
    
    def __str__(self):  
        return self.username