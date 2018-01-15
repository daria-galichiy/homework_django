from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин:')
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль:')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Повторите пароль:')
    email = forms.EmailField(widget=forms.EmailInput, label='E-mail:')
    surname = forms.CharField(label='Фамилия:')
    firstname = forms.CharField(label='Имя:')
