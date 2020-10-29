from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Contact, NewPost
from django import forms


User = get_user_model()


#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ("first_name", "last_name", "username", "email")


class ContactForm(forms.ModelForm):
    class Meta:
        # на основе какой модели создаётся класс формы
        model = Contact
        # укажем, какие поля будут в форме
        fields = ('name', 'email', 'subject', 'body')

    def clean_subject(self):
        data = self.cleaned_data['subject']

        if "спасибо" not in data.lower():
            raise forms.ValidationError("Вы обязательно должны нас поблагодарить!")
        return data


class PostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ('group', 'text')

    def clean_text(self):
        data = self.cleaned_data['text']

        if data == "":
            raise forms.ValidationError("А текст кто писать будет?!")
        return data
