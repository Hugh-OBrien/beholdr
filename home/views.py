from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader, RequestContext

def home(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render())
