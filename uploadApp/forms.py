from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # Делаем поле "name" необязательным к заполнению
    class Meta:
        model = Post
        fields = ['file_path', 'description']
