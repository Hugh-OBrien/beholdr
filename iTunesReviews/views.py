from django.http import HttpResponse
import itunesreviewreport
import io

from django.views.generic import TemplateView

class main(TemplateView):

    template_name= 'itunesreviews/main.html'

    #def get(self, request, *args, **kwargs):
     #   return render('/itunesreviews/main.html')
     
def runReport(request):
    
    idnumber = request.POST['id']

    
    report = itunesreviewreport.report(idnumber)
        
    response = HttpResponse(report ,content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="iTunesReviews.xls"'
    
    return response
        

#itunesreviewreport.report(903688996)