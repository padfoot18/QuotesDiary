from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(label='Password', max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=20, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(label='Password', max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    cnfm_pwd = forms.CharField(label='Confirm Password', max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
