from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm





class FarmUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email_address', 'type', 'is_staff', 'is_superuser')


class FarmUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()


class SignupForm(forms.Form):
    type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=False)

    def signup(self, request, user):
        user.type = self.cleaned_data['type']
        user.save()


