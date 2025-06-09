from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    model = models.CharField(max_length=100)
    manufacturing_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    plate = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    car_count = models.IntegerField()
    car_total_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.car_count} {self.car_total_value} {self.created_at}'
