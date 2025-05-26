from django.shortcuts import render, redirect

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
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
    else:
        form = CarForm()
    return render(request, 'create.html', {'form': form})
