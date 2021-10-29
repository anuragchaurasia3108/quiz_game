# created by Anurag

from django.http import HttpResponse
from django.shortcuts import render
import datetime
def index(request):
    return render(request,'index.html')
    # return HttpResponse('''<h1>nehal<h1> <a href="https://www.youtube.com/channel/UC2V7IhXeo_c6OFWSaoH1Urw"> anuragchannelplaylist</a>''')
def index1(request):
    return render(request,'index1.html')

def index2(request):
    current_datetime = datetime.datetime.now()
    tim = "Current Date and Time : %s " % current_datetime
    paras = {'time': tim}
    return render(request, 'index2.html', paras)

def ressult(request):
    return render(request, 'ressult.html')
def index3(request):
    return render(request,'index3.html')
def index4(request):
    return render(request,'index4.html')

