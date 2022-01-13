import logging
import smtplib

from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from website.forms import ContactForm

logger = logging.getLogger(settings.PROJECT_NAME)


# Create your views here.
def index_page(request):

    contact_form = ContactForm()
    email_fail = False
    contact_fail = False

    if request.method == 'POST' and 'contact' in request.POST:

        logger.info("Contact form was posted - %s", request.POST)

        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid() and contact_form.recaptcha_is_valid(request):

            logger.info("Contact form data was valid. Generating email")

            data = {}
            data['name']    = contact_form.cleaned_data['name']
            data['email']   = contact_form.cleaned_data['email']
            data['subject'] = contact_form.cleaned_data['subject']
            data['message'] = contact_form.cleaned_data['message']

            try:
                contact_form.send_email(data)

                response = HttpResponseRedirect('/')

                # Add cookie so we know succesful contact form was posted when handling redirect
                # Could pass this email to template (not doing it at the moment)
                response.set_cookie('provided_email', data['email'])

                return response

            except smtplib.SMTPException:
                logger.error("Error occured sending contact email")
                email_fail = True
        else:
            logger.error("Contact form data was invalid")
            contact_fail = True

    logger.info("Rendering index.html")

    # This means a successful contact form was posted
    if request.COOKIES.get('provided_email'):

        context_dict = {'contact_form': contact_form,
                        'contacted'   : True,
                        'email_fail'  : email_fail,
                        'contact_fail': contact_fail}

        response = render(request, 'index.html', context_dict)
        response.delete_cookie('provided_email')

        return response

    else:

        context_dict = {'contact_form': contact_form,
                        'contacted'   : False,
                        'email_fail'  : email_fail,
                        'contact_fail': contact_fail}

        return render(request, 'index.html', context_dict)
