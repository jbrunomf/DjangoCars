from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

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


class CarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'create.html'
    success_url = '/cars/'
    form_context_name = 'test'


class CarDetailView(DetailView):
    model = Car
    template_name = 'detail.html'
    context_object_name = 'car'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
