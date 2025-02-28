# myApp/forms.py
from django import forms
from .models import UserDetails,OwnerDetails, Service, Staff

class UserDetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'phone', 'password', 'gender', 'city', 'address_line', 'state', 'pincode', 'country','first_name','last_name','date_of_birth']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')

class OwnerDetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = OwnerDetails
        fields = ['username','first_name','last_name','salon_name', 'email', 'phone','gender','address','city','state','pin_code','country', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'position', 'email', 'phone', 'photo']

#class AppointmentForm(forms.ModelForm):
#    class Meta:
        # model = Appointment
        # fields = ['person_name', 'time_slot', 'category', 'service_name', 'status']
        # widgets = {
        #     'time_slot': forms.TextInput(attrs={'placeholder': 'e.g., 10:00 AM - 11:00 AM'}),
        # }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Time in minutes'}),
        }


