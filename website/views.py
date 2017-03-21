import logging
import smtplib

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from website.forms import ContactForm

logger = logging.getLogger('PersonalWebsite.website.views')


# Create your views here.
def indexPage(request):

    context = RequestContext(request)

    contact_form = ContactForm()
    email_fail   = False

    if request.method == 'POST' and 'contact' in request.POST:

        logger.info("Contact form was posted - %s", request.POST)

        contact_form = ContactForm(data = request.POST)

        if contact_form.is_valid():

            logger.info("Contact form data was valid. Generating email")

            data = {}
            data['name']    = contact_form.cleaned_data['name']
            data['email']   = contact_form.cleaned_data['email']
            data['subject'] = contact_form.cleaned_data['subject']
            data['message'] = contact_form.cleaned_data['message']

            try:
                contact_form.sendEmail(data)

                response = HttpResponseRedirect('/')

                # Add cookie so we know succesful was posted when handling redirect
                # Could pass this email to template (not doing it at the moment)
                response.set_cookie('provided_email', data['email'])

                return response

            except smtplib.SMTPException:
                logger.error("Error occured sending contact email")
                email_fail = True
        else:
            logger.error("Contact form data was invalid")

    logger.info("Rendering index.html")

    # This means a successful contact form was posted
    if request.COOKIES.get('provided_email'):

        context_dict = {'contact_form': contact_form,
                        'contacted'   : True,
                        'email_fail'  : email_fail}

        response = render_to_response('index.html', context_dict, context)
        response.delete_cookie('provided_email')

        return response

    else:

        context_dict = {'contact_form': contact_form,
                        'contacted'   : False,
                        'email_fail'  : email_fail}

        if email_fail:
            context_dict['email'] = data['email']

        return render_to_response('index.html', context_dict, context)
