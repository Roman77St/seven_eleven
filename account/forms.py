from django import forms
from django.contrib.auth.models import User



# class LoginForm(forms.Form):
#     username = forms.CharField(label='Имя пользователя')
#     password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не соответствуют друг другу')
        return cd['password2']
    


    
