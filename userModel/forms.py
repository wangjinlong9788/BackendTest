from django import forms
from django.http import HttpResponse

from django.contrib.auth.models import User
class LoginForm(forms.Form):
    usernames = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'your username'}))
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match')
        return cd['password2']
    def clean_email(self):
        cd= self.cleaned_data
        emails=cd['email']
        if emails  and User.objects.filter(email=emails).exists():
            raise forms.ValidationError(u'Please use a different email address.')
        if emails=='':
            raise forms.ValidationError(u'Please use an email address.')
        return emails
