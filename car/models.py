from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    manufacturing_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model
