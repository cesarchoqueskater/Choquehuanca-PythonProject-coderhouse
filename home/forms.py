from django import forms

class CreateBlog(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, required=False)
    publication_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    is_published = forms.BooleanField(required=False)
    tags = forms.CharField(required=False)

class SearchBlog(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    author = forms.CharField(max_length=100, required=False)