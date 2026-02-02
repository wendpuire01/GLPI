from django import forms
from .models import Ordinateur,Mouvement,Licences

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Ordinateur
        fields = ['marque','ram','dte_acquisition','disque_dur','processeur','ecran']



class AttributionForm(forms.ModelForm):
    class Meta :
        model = Mouvement
        fields=['ordinateur','utilisateur','motifs','date']
        
class LicenceForm(forms.ModelForm):
    class Meta:
        model = Licences
        fields = ['cle', 'uses_nbr', 'expiration_date']
       