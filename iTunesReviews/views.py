from django.http import HttpResponse
from django.template import loader, RequestContext
from django import forms
from os import path, chdir
import itunesreviewreport
import io

from django.views.generic import TemplateView

#class countries(forms.Form):
#
#    countryForm = forms.SelectMultiple(choices=countries)


def main(request):

    countryfile=0;

    #get the country list
    #run through the country list file and generate country objects with the country codes and names
    try:
        newPath = path.abspath(path.dirname(__file__))
        chdir(newPath)
        
    except Exception, e:
        return HttpResponse("can't open countryList, file missing from app folder 1")

    try:
        countryfile = open("countrylist.csv").readlines()
    except:
        return HttpResponse("can't open countryList, file missing from app folder")
    
    template = loader.get_template('itunesreviews/main.html')
    context = RequestContext(request, {'country_list' : countryfile,})
    return HttpResponse(template.render(context))
     
def runReport(request):
    
    idnumber = request.POST['id']
    countryList = request.POST.getlist('countryList[]')

    report = itunesreviewreport.report(idnumber,countryList)
        
    response = HttpResponse(report ,content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="iTunesReviews.xls"'
    
    return response
        

#itunesreviewreport.report(903688996)
