from dival_app.models import UserProfile
from django import forms


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    Email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta():
        model = UserProfile
        fields = ('username','password','Email')


class LoginForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('username','password')
