import logging
import smtplib

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings

from website.forms import ContactForm

logger = logging.getLogger('PersonalWebsite.website.views')


# Create your views here.
def indexPage(request):

    context = RequestContext(request)

    contact_form = ContactForm()
    email_fail   = False
    contact_fail = False

    if request.method == 'POST' and 'contact' in request.POST:

        logger.info("Contact form was posted - %s", request.POST)

        contact_form = ContactForm(data = request.POST)

        if contact_form.is_valid():

            logger.info("Contact form data was valid. Generating email")

            data = {}
            data['name']    = contactForm.cleaned_data['name']
            data['email']   = contactForm.cleaned_data['email']
            data['subject'] = contactForm.cleaned_data['subject']
            data['message'] = contactForm.cleaned_data['message']

            try:
                contact_form.sendEmail(data)

                return HttpResponseRedirect('/')

            except smtplib.SMTPException:
                logger.error("Error occured sending contact email")
                email_fail = True
        else:
            contact_fail = True
            logger.error("Contact form data was invalid")

    context_dict = {'contact_form': contact_form,
                    'contact_fail': contact_fail,
                    'email_fail'  : email_fail}

    return render_to_response('index.html', context_dict, context)
