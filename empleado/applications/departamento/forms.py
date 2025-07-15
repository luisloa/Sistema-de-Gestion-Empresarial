from django import forms

class NewDepartForm(forms.Form):
    dpto = forms.CharField(max_length=50, required=True)
    short_dpto = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
        