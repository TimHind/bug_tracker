from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=280)
    description = forms.CharField(max_length=280)