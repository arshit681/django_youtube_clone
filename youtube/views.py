
from asyncio import get_running_loop
from re import template
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .forms import getname


from .models import Item
# class SearchResultsView(ListView):
#     model = Item.name
#     template_name = 'sample.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         object_list = Item.objects.filter(Q(name__icontains=query))
#         return object_list

# def home_view(request):
#     if request.method=='POST':
#         data=getname(request.POST)
#         print(data)
#     else:
#         data=getname()
#         print("from get request")
#     return render(request, "sample.html", {'form':data})
# def result(request):
#     result = request.GET['q']
#     print(result)
#     return render(request, 'sample.html', {result})

def filter(request):
    # print(request)
    
    return render(request)
    
def home(request):
    vids=Item.objects.all()
    if request.method == 'GET':
        input_data= request.GET.get('textbox')
        print()
        if input_data is not None:
            results=Item.objects.filter(Q(name__contains=input_data)|Q(description__contains=input_data))
            return render(request, 'sample.html',{'vids':results })
        else:
            return render(request, 'sample.html',{'vids':vids })
    else:
        return render(request, 'sample.html',{'vids':vids })
    # print("data", data)
    # vid1=Item()
    # vid1.Y_id='YpTmcCBBdTE'
    # vid2=Item()
    # vid2.Y_id="d2na6sCyM5Q"
    # vid3=Item()
    # vid3.Y_id='2Ji-clqUYnA'
    # vids=[vid1,vid2,vid3]
   
    # print(vids)
    

    

# Create your views here.
