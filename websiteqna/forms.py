from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class signupform(UserCreationForm):
    password1 = forms.CharField(label=('Password'), widget=forms.PasswordInput, strip=False)
    password2 = forms.CharField(label=("Password Confirmation"), widget=forms.PasswordInput, strip=False)
    email = forms.EmailField(max_length=50, required=False, label='Email Address*', widget=forms.TextInput(attrs={'placeholder': '(Optional)'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']
        help_texts = {
        'username': None,
        } 
                      

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('this username already taken!')
        return username 

    def clean_email(self):
        email = self.cleaned_data.get('email') 
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('this email already registered!')
        return email     

        

class contactform(forms.Form):
    from_email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    
    
        
