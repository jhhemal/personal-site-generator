from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

from functools import partial
DateInput = partial(forms.DateInput, {'class' : 'datepicker', 'placeholder' : 'Enter Date'})

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'mobile_no', 'image', 'dob', 'location', 'password1', 'password2']

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'placeholder' : 'Enter Your First name'
            }),
            'last_name' : forms.TextInput(attrs={
                'placeholder' : 'Enter Your Last name'
            }),
            'email' : forms.EmailInput(attrs={
                'placeholder' : 'Enter Your email'
            }),
            'username' : forms.TextInput(attrs={
                'placeholder' : 'Enter Your username'
            }),
            'mobile_no' : forms.NumberInput(attrs={
                'placeholder' : 'Enter your number here.'
            }),
            'image' : forms.FileInput(attrs={
                'class' : 'custom-file-input',
                'id' : 'inputGroupFile02',
            }),
            'dob' : DateInput(),
            'location' : forms.TextInput(attrs={
                'placeholder' : "Enter Location, like Seoul, South Korea"
            }),
            'password1' : forms.PasswordInput(attrs={
                'placeholder' : "Enter Password"
            }),
            'password2' : forms.PasswordInput(attrs={
                'placeholder' : "Re-Enter Password"
            })
        }


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder' : "Type Your Password"
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder' : "Re-Type Your Password"
        })
        self.fields['dob'].required = False

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widgets = forms.TextInput(attrs={
            'placeholder' : 'Enter your username'
        })
        self.fields['password'].widgets = forms.TextInput(attrs={
            'placeholder' : 'Enter your password'
        })