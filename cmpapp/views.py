from django.shortcuts import render,HttpResponse
#from .models import CompanyList
from mainapp.models import CompanyName

# Create your views here.
def cmplist(request):
    company_name_list = CompanyName.objects.order_by('id')
    context = {
        'company_name_list' : company_name_list
    }
    return render(request, 'cmpapp/cmplist.html', context)

def cmp(request, company_id):
    return HttpResponse("cmp")