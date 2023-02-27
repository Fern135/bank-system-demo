from django import forms

class ContactForm(forms.Form):
    full_name   = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter full name'}), required=True)
    emailid     = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter email id'}), required=True)
    subject     = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter subject'}), required=True)
    message     = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Message'}), required=True)