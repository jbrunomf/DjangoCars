from django import forms
from car.models import Brand, Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all())
    manufacturing_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=7)
    value = forms.DecimalField()
    image = forms.ImageField()

    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            manufacturing_year=self.cleaned_data['manufacturing_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            image=self.cleaned_data['image'],
        )
        car.save()
        return car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
