from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    subject = forms.CharField()
    email = forms.EmailField()
