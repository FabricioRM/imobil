from django import forms
from .models import Locatario
from .models import Imovel

## Cadastra Cliente          
class LocatarioForm(forms.ModelForm):
    class Meta:
        model = Locatario
        fields = '__all__'
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'

## Cadastra um Imovel
class ImovelForm(forms.ModelForm):
    Imovel = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Imovel
        fields = '__all__'
        exclude = ('is_locate',)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'