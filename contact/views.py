# ------------- Libraries and Modules --------------------------------
# Django
from django.shortcuts import render, redirect # Render HTML, and redirect to another page
from django.views import View # Create class-based views
from django.core.mail import EmailMessage # Email Sender
from django.template.loader import render_to_string # Template loader
from django.conf import settings # Django Settings
from django.contrib import messages # Messages
# ---------------------- Views ---------------------------
"""
    Render a contact form page
"""
class ContactView(View):
    def get(self, request):
        return render(request, 'contact/contact.html')

"""
    View image for sending an Email message, that the user give us
"""
class SendEmailView(View):
    # Post view
    def post(self, request):
        # Data from user
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Email template config
        template = render_to_string('contact/email.html', {
            'name': name, 
            'email': email,
            'message': message
        })
        # Create the email
        email = EmailMessage(
            "Portfolio Email", 
            template,
            settings.EMAIL_HOST_USER, # Email sender
            ['dricardosc15@gmail.com'] # Email reciever
        )
        # Send the email
        email.fail_silently = False
        email.send()
        # Send a message to the web page
        messages.success(request, 'Your mail has been sent successfully')
        # Redirect to the contact form view
        return redirect('contact:contact_form')


"""
MIT License

Copyright (c) 2022 Daniel Ricardo Sequeira Campos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""