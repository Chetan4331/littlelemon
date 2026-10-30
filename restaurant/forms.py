from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_slot']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Your Name', 'id': 'first_name'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'id': 'reservation_date'}),
            'reservation_slot': forms.Select(attrs={'id': 'reservation_slot'}),
        }
