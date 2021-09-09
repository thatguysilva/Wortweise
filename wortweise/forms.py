from .models import Comment
from django import forms
from django.forms import TextInput



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message')
        message = forms.CharField(widget=forms.Textarea)
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'message': forms.Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Kommentar'
                })
        }
 
 
    def __init__(self, *args, **kwargs):
    	super(CommentForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
    	self.fields['name'].widget.attrs['style'] = 'width:100%; height:25px;'
    	self.fields['message'].widget.attrs['style']  = 'width:100%; height:100px;'


