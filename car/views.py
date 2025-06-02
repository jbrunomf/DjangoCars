from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from car.models import Car
from car.forms import CarModelForm


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            queryset = super().get_queryset().filter(model__icontains=self.request.GET.get('search'))
        else:
            queryset = super().get_queryset().order_by('model')
        return queryset


class NewCarView(View):
    def get(self, request):
        form = CarModelForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
        return render(request, 'create.html', {'form': form})
