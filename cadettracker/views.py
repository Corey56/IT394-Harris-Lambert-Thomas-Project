from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Company, Location, Supply, Personnel, Regiment, CompanyHasSupply, RegHasSupply, Building, CompanyNeedsSupply


# Create your views here.

def index(request):
    Company_list = Company.objects.order_by('CompanyName')
    Reg_List = Regiment.objects.order_by('RegNum')
    #output = ', '.join([(str(c.CompanyName) + ": " + str(c.regiment) + "  " + str(c.LocationID))
                       # for c in Company_list])
    template = loader.get_template('cadettracker/index.html')
    context = {
        'Company_list': Company_list,
        'Reg_List': Reg_List,
    }
    return HttpResponse(template.render(context,
                                        request))

def company(request,company_id):
    Co = Company.objects.get(pk=company_id)
    #import pdb
    #pdb.set_trace()
    template = loader.get_template('cadettracker/company.html')
    context = {
        'Co' : Co,
    }
    return HttpResponse(template.render(context,
                                        request))

#List cadets is first view
'''
def index(request):
    cadets = Cadet.objects.all()
    context = {'cadets': cadets}
    template = loader.get_template('cadettracker/index.html')
    return HttpResponse(template.render(context,request))
'''
