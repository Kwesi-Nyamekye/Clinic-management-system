from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "age", "gender", "detail", "medicine_detail", "amount", "next_visit"]

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "age", "gender", "detail", "medicine_detail",  "mobile", "address", "amount", "note", "next_visit"]

    def __init__(self, *args, **kwargs):
        super(AddPatientForm, self).__init__(*args, **kwargs)
        self.fields['address'].required=False 
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })