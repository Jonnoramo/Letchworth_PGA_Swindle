from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')   
    membership_id = forms.CharField(label='Membership ID')
    handicap = forms.CharField(label='handicap')
    user_profile_picture = forms.ImageField(label= 'Profile picture', required="False")
    house_number = forms.CharField(label= 'House Number')
    street = forms.CharField(label= 'Street')
    city = forms.CharField(label= 'city')
    occupation = forms.CharField(label= 'Occupation')


    class Meta:
		model = User
		fields = ['email', 'user_profile_picture', 'first_name', 'last_name', 'handicap', 'membership_id', 'city', ]

    def clean_email(self):
		email = self.cleaned_data.get('email')

		if not email:
			message = "Please enter a valid email address"
			raise forms.ValidationError(message)

		return email
		
class UserLoginForm(forms.Form):
    email = forms.EmailField()	
    password = forms.CharField(widget=forms.PasswordInput)	

    