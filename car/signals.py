from django.db.models.aggregates import Sum
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver

from car.models import CarInventory


@receiver(pre_save, sender='car.Car')
def car_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")


@receiver(post_save, sender='car.Car')
def car_post_save(sender, instance, *args, **kwargs):
    print('Calculando valor do inventário..')
    cars = sender.objects.all()
    total_value = cars.aggregate(Sum('value'))['value__sum'] or 0
    car_count = len(cars)
    CarInventory.objects.create(
        car_count=car_count,
        car_total_value=total_value
    )
