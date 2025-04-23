from django import forms
from .models import person

class personform(forms.ModelForm):
    class Meta:
        model = person
        fields = ['first_name','last_name','gmail','phone_number','position_applied','experience','application_status']
        widgets = {
            'application_status': forms.Select(choices=person.STATUS_CHOICES),
               # หรือถ้าคุณต้องการระบุ widgets หรือ labels เอง
        }
