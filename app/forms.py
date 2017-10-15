from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Name', max_length=128)
	email = forms.EmailField(label='Email')
	phone = forms.CharField(label='Phone', max_length=64)
	subject = forms.CharField(label='Subject')
	message = forms.CharField(label='Message', widget=forms.Textarea)