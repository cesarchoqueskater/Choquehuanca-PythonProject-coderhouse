from django import forms
from home.models import Blog


class CreateBlog(forms.Form):
    title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    author = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    publication_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class' : 'form-control'}), required=False)
    is_published = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'type': 'checkbox','class': 'form-check-input'}))
    tags = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))

class SearchBlog(forms.Form):
    title = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))

#class UpdateBlog(forms.Form):
class UpdateBlog(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }            
    #title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    #author = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    #publication_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class' : 'form-control'}), required=False)
    #is_published = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'type': 'checkbox','class': 'form-check-input'}))
    #tags = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'})) 