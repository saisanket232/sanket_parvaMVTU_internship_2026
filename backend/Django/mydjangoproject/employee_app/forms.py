from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name cannot contain numbers or special characters")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be a gmail address")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must be a digit")
        return phone

    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary < 0:
            raise forms.ValidationError("Salary cannot be negative")
        return salary