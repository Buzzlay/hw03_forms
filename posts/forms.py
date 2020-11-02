from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text')

    def clean_text(self):
        data = self.cleaned_data['text']
        f_word = 'козёл'
        # Если появится время можно написать фильтр мата, тема стара как мир - информации много (как это сделать)
        if f_word in data:
            raise forms.ValidationError("У нас приличное сообщество - попрошу не выражаться!")
        return data
