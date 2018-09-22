from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"fullname"}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"email"}))
	details = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"details"}))


	#def clean_email(self):
	#	email = self.clean_data.get("email")
	#	if not "gmail.com" in email:
	#		raise forms.ValidationError("Email has to be gmail")
	 #   return email		