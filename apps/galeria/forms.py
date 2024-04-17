from django import forms
from apps.galeria.models import Fotografia

#Neste caso vamos fazer um form baseado no nosso models
class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia # aqui pega a que model ele quer fazer os forms
        exclude = ['publicada',] #único campo que não quero no meu form
        labels = {
            'descricao': 'Descrição',
            'data_foto': 'Data de Registro',
            'usuario': 'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_foto': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                    }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }

