from django.forms import ModelForm

from .models import Estudante

''''classe para importar'''

class EstudanteForm(ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'CPF', 'email', 'idade', 'bio']