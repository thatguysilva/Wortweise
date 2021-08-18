from .models import Comment
from django import forms
from django.forms import TextInput



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'body': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Your message'
                })
        }
 
 
    def __init__(self, *args, **kwargs):
    	super(CommentForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
    	self.fields['name'].widget.attrs['style'] = 'width:400px; height:25px;'
    	self.fields['body'].widget.attrs['style']  = 'width:700px; height:100px;'


