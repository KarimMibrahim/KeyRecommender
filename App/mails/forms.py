from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea, required=False)
    subject = forms.CharField(required=False)
    email = forms.EmailField(required=False)
