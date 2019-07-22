from django import forms

class ContactForm(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(
		attrs={
		"class" : "form-control",
		"placeholder" : "Your Full Name",
		}))

	email = forms.EmailField(widget=forms.EmailInput(
		attrs={
		"class" : "form-control",
		"placeholder" : "Type Your eMail Here"
		}))

	content = forms.CharField(widget=forms.Textarea(
		attrs={
		"class" : "form-control",
		"placeholder" : "Type Your Text Here"
		}))

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com":
			raise forms.ValidationError("Email is wrong try again..!")
		return email

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={
		"class" : "form-control",
		"placeholder" : "Enter Your username",
		}))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
		"class" : "form-control",
		"placeholder" : "Enter Your password",
		}))