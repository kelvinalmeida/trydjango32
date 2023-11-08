from django import forms

class ArticleForm(forms.Form):
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
