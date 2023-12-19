from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_topic(request):
    DLTO=Topic.objects.all()
    DLTO=Topic.objects.all().order_by('topic_name')
    

    d={'topics':DLTO}
    return render(request,'display_topic.html',context=d)
def display_webpage(request):
    DLWO=Webpage.objects.all()
    DLWO=Webpage.objects.order_by('name')
    DLWO=Webpage.objects.order_by('-name')
    DLWO=Webpage.objects.all().order_by(Length('name'))
    DLWO=Webpage.objects.all().order_by(Length('name').desc())
    DLWO=Webpage.objects.filter(topic_name='Cricket')
    DLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    DLWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    DLWO=Webpage.objects.exclude(topic_name='Cricket')
    DLWO=Webpage.objects.exclude(topic_name='Cricket').order_by('name')
    DLWO=Webpage.objects.exclude(topic_name='Cricket').order_by('-name')
    DLWO=Webpage.objects.exclude(topic_name='Cricket').order_by(Length('name'))
    DLWO=Webpage.objects.all()[2:6]
    DLWO=Webpage.objects.all()
    DLWO=Webpage.objects.filter(name__startswith='r')
    DLWO=Webpage.objects.filter(name__endswith='u')
    DLWO=Webpage.objects.filter(developer_name__contains='i')
    DLWO=Webpage.objects.filter(topic_name__in=('football','kabadi'))
    DLWO=Webpage.objects.filter(topic_name__in=['football','Cricket'])
    DLWO=Webpage.objects.filter(name__regex='\w+u$')

    


    d={'webpages':DLWO}
    return render(request,'display_webpages.html',context=d)

def display_accessrecord(request):
    DLAO=AccessRecord.objects.all()
    DLAO=AccessRecord.objects.filter(id=4)
    DLAO=AccessRecord.objects.filter(id__gt=2)
    DLAO=AccessRecord.objects.filter(id__gte=4)
    DLAO=AccessRecord.objects.filter(id__lte=4)
    DLAO=AccessRecord.objects.filter(id__lt=4)
    DLAO=AccessRecord.objects.filter(date__gte='2023-12-19')
    DLAO=AccessRecord.objects.filter(date__lt='2023-12-19')
    DLAO=AccessRecord.objects.filter(date__month='12')
    DLAO=AccessRecord.objects.filter(date__year='2022')
    DLAO=AccessRecord.objects.filter(date__day__lte='19')
    
    d={'accessrecord':DLAO}
    return render(request,'display_accessrecord.html',context=d)


def insert_topic(request):
    a =input('enter data: ')
    TOPOBJ=Topic.objects.get_or_create(topic_name=a)[0]
    TOPOBJ.save()
    data = Topic.objects.all()
    d = {'topics':data}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    a =input('enter topic name : ')

    to = Topic.objects.get(topic_name = a)
    n = input('Enter name: ')
    u = input('Enter url: ')
    dn = input('Enter devr name: ')

    TOPOBJ=Webpage.objects.get_or_create(topic_name=to,name = n,url = u,developer_name = dn)[0]
    TOPOBJ.save()
    data = Webpage.objects.all()
    d = {'webpages':data}
    return render(request,'display_webpages.html',d)

def del_topic(request):
    a = input('Enter topic name : ')
    TO = Topic.objects.get(topic_name = a)

    TO.delete()

    QS = Topic.objects.all()
    d = {'topics':QS}

    return render(request,'display_topic.html',context=d)
