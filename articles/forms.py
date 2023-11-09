from typing import Any
from django import forms

from .models import ArticleModel

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'content']


    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = ArticleModel.objects.all().filter(title__contains=title)

        if qs.exists(): 
            self.add_error('title', f'Já existe titulo com esse nome \"{title}\"')

        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


    # def clean_title(self):
    #     title = self.cleaned_data.get('title')

    #     if 'office' in title:
    #         raise forms.ValidationError('O titolo não pode ter "office"!')

    #     return title
    

    def clean(self):
        cleaned_data = self.cleaned_data
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')

        if 'office' in title:
            self.add_error('title', 'contem office no titulo')
            raise forms.ValidationError('O titolo não pode ter "office"!')
        
        if 'office' in content:
            self.add_error('content', 'contem office no content')
            raise forms.ValidationError('O content não pode ter "office"!')
            # raise forms.ValidationError('O content não pode ter "office"!')

        return cleaned_data
