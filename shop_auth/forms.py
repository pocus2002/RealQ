from django import forms
from .models import ShopUser

class ShopUserCreateForm(forms.ModelForm):

    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ShopUser
        # fields = ['email', 'password', 'nickname']
        fields = ['email', 'nickname', 'password', 'password_confirm']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user