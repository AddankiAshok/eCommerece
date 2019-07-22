from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
	context = {
	"title" : "Welcome to the Home Page",
	"content" : "Hello there youre in Home Page"
	}
	if request.user.is_authenticated():
		context["premium_content"] = "Congratulations Successfully Loggedin"
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	"title" : "Welcome to the Contact Page",
	"content" : "Hello there youre in Contact Page",
	"contact_form" : contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method == "POST":
	# 	print(request.POST.get("fullname"))
	# 	print(request.POST.get("email"))
	# 	print(request.POST.get("content"))

	return render(request, "contact/view.html", context)

def about_page(request):
	context = {
	"title" : "Welcome to the About Page",
	"content" : "Hello there youre in About Page"
	}
	return render(request, "about.html", context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
	"form" : form
	}
	print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		context["form"] = LoginForm()
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
	
	return render(request, "auth/login.html", context)

def register_page(request):
	
	return render(request, "register.html", context)
