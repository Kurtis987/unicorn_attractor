from django import forms
from .models import FeatureReqeust, Post
 
 
class FeatureRequestForm(forms.ModelForm):
    name = forms.CharField(label="Feature Request name") 
    is_a_poll = forms.BooleanField(label=('Include a poll?'),
    widget=forms.HiddenInput(), required=False, initial=True)
    #is_a_poll = True
    class Meta:
        model = FeatureRequest
        fields = ['name']
 
 
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['comment']