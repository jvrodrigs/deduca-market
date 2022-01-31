from django.db import models
from django.conf import settings

# Create your models here.

# Responsible (Responsável pelo produto) 
# Creation (Data de criação do produto)
# Title
# Content
# Price

class Product(models.Model):
    class Meta:
        db_table = 'product'
    
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title
