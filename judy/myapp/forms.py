from django import forms
from .models import person

class personform(forms.ModelForm):
    class Meta:
        model = person
        fields = ['first_name','last_name','gmail','phone_number','position_applied','experience']
        widgets = {
            'application_status': forms.Select(choices=person.STATUS_CHOICES),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.application_status = 'waiting' #รอสัมภาษณ์อัตโนมัติ
        if commit:
            instance.save()
        return instance

class EditForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ['first_name', 'last_name', 'gmail', 'phone_number', 'position_applied', 'experience', 'application_status']
        widgets = {
            'application_status': forms.Select(choices=person.STATUS_CHOICES),
        }
