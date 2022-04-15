from django import forms
from.models import contactus
from.models import Booking


class contact(forms.ModelForm):
    class Meta:
        model = contactus
        fields= "__all__"
    
class fixed(forms.ModelForm):
    class Meta:
        model = Booking
        fields= "__all__"
        
