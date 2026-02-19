from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_price_in_euros(self):
        return f'{self.price} €'
    def get_description_in_euros(self):
        return f'{self.name} - {self.price} €'
    
    def __str__(self):
        return self.name
