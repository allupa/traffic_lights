from django import forms  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#from .models import Sensor 
   
   
#class SensorForm(forms.ModelForm):
#     class Meta:  
#         model = Sensor  
#         fields = ['sensor_id', 'crossroad']  

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 
                  'first_name', 
                  'last_name',
                  'email',
                  'password1'
                  )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user