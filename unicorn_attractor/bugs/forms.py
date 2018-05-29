from django import forms
from .models import Bug, Post
 
 
class BugForm(forms.ModelForm):
   class Meta:
       model = Bug
       fields = ['name']
 
 
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['comment']