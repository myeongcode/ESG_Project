from django.shortcuts import render
from .models import CompanyName

# Create your views here.
def main(request):
    company_name_list = CompanyName.objects.order_by('id')
    context = {
        'company_name_list' : company_name_list
    }
    return render(request, 'mainapp/main.html', context)