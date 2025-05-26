from PIL.Image import blend
from django import forms
from car.models import Brand


class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    manufacturing_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=7)
    value = forms.DecimalField()
    photo = forms.ImageField()
