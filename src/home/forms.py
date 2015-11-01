__author__ = 'Hedi Chahed'
from django import forms
from home.models import client


class ClientForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ('FIRST_NAME','LAST_NAME','ADDRESS_LINE_1','ADDRESS_LINE_2', 'TOWN_CITY','REGION_STATE','COUNTRY','POST_CODE','EMAIL_ADRESS','PHONE_NUMBER')

