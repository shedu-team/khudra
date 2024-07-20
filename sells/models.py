from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} _ ({self.price})"



