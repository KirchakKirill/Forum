from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError


# class RegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'required': 'True', 'placeholder': 'Username'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'required': 'True', 'placeholder': 'Email'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'True', 'placeholder': 'Password'}),
#                                 min_length=8)
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'required': 'True', 'placeholder': 'Confirm password'}), min_length=8)
#
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'password1', 'password2']
#
#     def email_clean(self):
#         email = self.cleaned_data.get('email')
#         if email and self._meta.model.objects.filter(email__iexact=email).exists():
#             raise ValidationError("This email already exists")
#         return email


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'required': 'True', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': 'True', 'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'True', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'True', 'placeholder': 'Last name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'True', 'placeholder': 'Password'}),
                                min_length=8)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': 'True', 'placeholder': 'Confirm password'}), min_length=8)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def email_clean(self):
        email = self.cleaned_data.get('email')
        if email and self._meta.model.objects.filter(email__iexact=email).exists():
            raise ValidationError("This email already exists")
        return email


class AuthenticationUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'required': 'True', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': 'True', 'placeholder': 'Password'}),
                               min_length=8)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
