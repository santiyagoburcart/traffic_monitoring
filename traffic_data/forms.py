# traffic_data/forms.py
from django import forms

class TrafficDataForm(forms.Form):
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))
    ip_address_v4 = forms.GenericIPAddressField(label='IPv4 Address', protocol='IPv4')
    ip_address_v6 = forms.GenericIPAddressField(label='IPv6 Address', protocol='IPv6')
