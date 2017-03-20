import smtplib
import logging
from email.mime.text import MIMEText

from django.conf import settings
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


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

    def sendEmail(self, data):

        sender    = settings.EMAIL_HOST_USER
        receivers = [sender]

        smtpObj = smtplib.SMTP(settings.EMAIL_HOST, 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(sender, settings.EMAIL_HOST_PASSWORD)

        msg = MIMEText(data['message'])
        msg['Subject'] = data['subject']
        msg['From']    = data['email']
        msg['To']      = settings.EMAIL_HOST_USER

        logger.debug("Sending %s email to %s", msg['Subject'], data['email'])

        smtpObj.sendmail(sender, receivers, msg.as_string())
        smtpObj.close()
