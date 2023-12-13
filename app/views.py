from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    DLTO=Topic.objects.all()
    d={'topics':DLTO}
    return render(request,'display_topic.html',context=d)
def display_webpage(request):
    DLWO=Webpage.objects.all()
    d={'webpages':DLWO}
    return render(request,'display_webpages.html',context=d)

def display_accessrecord(request):
    DLAO=AccessRecord.objects.all()
    d={'accessrecord':DLAO}
    return render(request,'display_accessrecord.html',context=d)
