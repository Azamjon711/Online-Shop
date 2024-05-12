from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name
