from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name=models.Charfield(max_length = 100)
    
