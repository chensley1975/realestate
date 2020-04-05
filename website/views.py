from django.shortcuts import render
from realestate.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def home(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def houses(request):
	return render(request, 'houses.html', {})

def contact(request):
	if (request.POST):
		email_data = request.POST.dict()
		firstName = email_data.get('fname')
		lastName = email_data.get('lname')
		email = email_data.get('email')
		phone = email_data.get('phone')
		question = email_data.get('question')
		subject = email_data.get('subject')
		subject = "New Contact from Website"
		message = "New question from your Website:<br/>First Name: " + str(firstName) + "<br/>Last Name: " + str(lastName) + "<br/>Email Address: " + str(email) + "<br/>Phone Number: " + str(phone) + "<br/>Contact Type: " + str(question) + "<br/>Comment: " + str(subject)
		send_mail(subject, message, EMAIL_HOST_USER, ['chensley@porchandgable.com'], fail_silently = False)
		return render(request, 'contact.html', {})
	return render(request, 'contact.html', {})