#import Django bits needed
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import TemplateView

import simplecast as simp


#inital form page
def listenByEpisode(request):
    result = True
    try:
        pod = request.POST['pod']
        date = request.POST['date']
    except:
        pod = ''
        date = ''
        result = False
    
    template = loader.get_template('simplecast/listens.html')

    #check if this is the first, otherwise run the simplecast api app
    if result:
        context = RequestContext(request, {'results' : simp(pod,date,date), \
                                           'pod':pod,'date':date})
    else:
        context = RequestContext(request, {'pod':pod,'date':date})
    
    return HttpResponse(template.render(context))
        
