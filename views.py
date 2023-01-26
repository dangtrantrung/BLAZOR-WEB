from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import  Question

# Create your views here.
def index (request):
    myname= 'Trung'
    taisanitem=['Điện thoại','Máy tính','Máy bay', 'Xe hoi', "Money"]
    context={'name':myname,'taisan':taisanitem}
    return  render(request,'polls/index.html',context)

def sanpham (request):
    return  HttpResponse('<h2>Danh sach san pham</h2')

def viewlist(request):
    #get_object_or_404(Question,pk=1)
    listQuestion=Question.objects.all()
    list=[x for x in listQuestion]
    listcount=len(list)
    context={'dsquest':listQuestion,'Numofquestion':listcount}
    return render(request,'polls/Questionlist.html',context)