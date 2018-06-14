from django import forms
from .models import Feature, Post
 
 
class FeatureForm(forms.ModelForm):
    name = forms.CharField(label="Feature name") 
    is_a_poll = forms.BooleanField(label=('Include a poll?'),
    widget=forms.HiddenInput(), required=False, initial=True)
    #is_a_poll = True
    class Meta:
        model = Feature
        fields = ['name']
 
 
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['comment']