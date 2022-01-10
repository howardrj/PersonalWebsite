import logging
import urllib
import urllib2
import json

from django.conf import settings
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail


logger = logging.getLogger('PersonalWebsite.website.forms')


def isValidEmail(email):

    try:
        validate_email(email)
        return True

    except ValidationError:
        return False


class ContactForm (forms.Form):

    name    = forms.CharField(label="Name", widget=forms.TextInput())
    email   = forms.EmailField(label="Email", widget=forms.TextInput())
    subject = forms.CharField(label="Subject", widget=forms.TextInput())
    message = forms.CharField(label="Message", widget=forms.Textarea())

    def __init__(self, *args, **kwargs):

        logger.debug("ContactForm constructor called")

        # Access base class constructor
        super(ContactForm, self).__init__(*args, **kwargs)

    def clean(self):

        name    = self.cleaned_data.get('name')
        email   = self.cleaned_data.get('email')
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')

        if not name or not email or not subject or not message:
            if not name:
                logger.debug("Name was not provided in contact form")
            if not email:
                logger.debug("Email was not provided in contact form")
            if not subject:
                logger.debug("Subject was not provided in contact form")
            if not message:
                logger.debug("Message was not provided in contact form")

            return self.cleaned_data

    def send_email (self, data):

        sender    = settings.EMAIL_HOST_USER
        receivers = [sender, ]

        logger.debug("Sending %s email to %s from %s", data['subject'], receivers, data['email'])

        subject = "Contact Message from %s - %s" % (data['email'], data['subject'])

        send_mail(subject, data['message'], sender, receivers)

    def recaptcha_is_valid (self, request):

        logger.debug("Validating reCAPTCHA")

        recaptcha_response = request.POST.get('g-recaptcha-response')

        url = 'https://www.google.com/recaptcha/api/siteverify'

        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }

        data = urllib.urlencode(values)

        req = urllib2.Request(url, data)

        response = urllib2.urlopen(req)

        result = json.load(response)

        valid = ('success' in result and result['success'])

        logger.debug("reCAPTCHA is %s" % ('valid' if valid else 'invalid'))

        return valid
