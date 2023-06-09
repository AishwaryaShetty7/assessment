from django import forms
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'



class PictureForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class UploadFileForm(forms.Form):
    file = forms.FileField()