from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text')

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == "":
            raise forms.ValidationError("А текст кто писать будет?!")
        return data
