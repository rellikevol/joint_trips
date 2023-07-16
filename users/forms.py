from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ChangeUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'prefer_conversations',
                  'prefer_music', 'prefer_smoke', 'prefer_animals']