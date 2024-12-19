from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Polls.models import Computer

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['status', 'reserved_by', 'reserved_from', 'reserved_until']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Извлекаем пользователя из аргументов
        super().__init__(*args, **kwargs)
        
        if user and not self.instance.reserved_by:  # Устанавливаем reserved_by только если он не установлен
            self.fields['reserved_by'].initial = user
        
        # Делаем поле reserved_by некликабельным
        self.fields['reserved_by'].widget.attrs['disabled'] = 'disabled'

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        reserved_until = cleaned_data.get("reserved_until")
        reserved_from = cleaned_data.get("reserved_from")

        if status == 'reserved':
            if not reserved_from or not reserved_until:
                raise forms.ValidationError("Укажите время начала и окончания бронирования.")
            if reserved_from >= reserved_until:
                raise forms.ValidationError("Время окончания должно быть позже времени начала.")
        
        return cleaned_data


