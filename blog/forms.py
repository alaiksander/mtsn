from django import forms

from .models import Post, Guru

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

class GuruForm(forms.ModelForm):

	class Meta:
		model = Guru
		fields = '__all__'