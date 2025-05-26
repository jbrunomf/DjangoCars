from django import forms
from car.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    """"
    Valida se o veículo foi enviado com valor mínimo de R$ 10000,00. (RN001).
    """

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 10000:
            self.add_error('value', 'Valor mínimo do veículo deve ser de R$ 10000,00.')
        return value


    """
    Valida o ano de fabricação. (RN002).
    """
    def clean_manufacturing_year(self):
        year = self.cleaned_data['manufacturing_year']

        if year < 2000:
            self.add_error('manufacturing_year', 'O ano de fabricação mínimo é 2000.')
        return year
