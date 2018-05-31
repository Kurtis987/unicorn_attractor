from django import forms
from .models import Bug, Post
 
 
class BugForm(forms.ModelForm):
    name = forms.CharField(label="Bug name") 
    is_a_poll = forms.BooleanField(label=('Include a poll?'),
    widget=forms.HiddenInput(), required=False, initial=True)
    #is_a_poll = True
    class Meta:
        model = Bug
        fields = ['name']
 
 
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['comment']