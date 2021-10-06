from django import forms

from medicines.models import Medicine


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['user', 'medicine_name', 'dosage', 'frequency']
