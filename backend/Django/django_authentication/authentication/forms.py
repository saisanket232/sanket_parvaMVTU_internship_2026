from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        
        if password != confirm:
            raise forms.ValidationError("Passwords do not match")