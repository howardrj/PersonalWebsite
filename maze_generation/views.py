# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def maze_generation_page(request):

    context_dict = {}

    context = RequestContext(request)

    return render_to_response('maze.html', context_dict, context)
