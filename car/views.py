from django.shortcuts import render

from car.models import Car

from car.forms import CarForm


def cars_list(request):
    cars = Car.objects.all()
    search_str = request.GET.get('search')

    if search_str:
        cars = Car.objects.filter(model__icontains=search_str)

    ctx = {'cars': cars}
    return render(request, template_name='cars.html', context=ctx)


def new_car(request):
    form = CarForm()
    return render(request, 'create.html', {'form': form})
