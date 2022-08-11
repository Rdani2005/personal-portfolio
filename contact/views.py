from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

class ContactView(View):
    def get(self, request):
        return render(request, 'contact/contact.html')

class SendEmailView(View):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        template = render_to_string('contact/email.html', {
            'name': name, 
            'email': email,
            'message': message
        })

        email = EmailMessage(
            "Portfolio Email",
            template,
            settings.EMAIL_HOST_USER,
            ['dricardosc15@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Your mail has been sent successfully')

        return redirect('contact:contact_form')