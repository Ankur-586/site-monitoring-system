from django import forms

class loginform(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))