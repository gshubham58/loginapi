from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail
from rest_framework.response import Response
from .serializer import DetailSerializer,ObjectSerailzer
from rest_framework.views import APIView

# Create your views here.
def index(request):
    return HttpResponse("Welcome")
def add(request,ud,pd):
    x=Detail.objects.filter(username=ud).count()
    if(x==0):
        a=Detail(username=ud,password=pd)
        a.save()
        return JsonResponse({'status':'success'})
    else:
       return JsonResponse({'status':'username already available'})
class list(APIView):
    def get(self,request):
        De=Detail.objects.all()
        serial=DetailSerializer(De,many=True)
        return Response(serial.data)
class list2(APIView):
    def get(self,request,ud):
        try:
            dea=Detail.objects.filter(username=ud)
            sera=ObjectSerailzer(dea,many=True)
            return Response(sera.data)
        except:
            return JsonResponse({'status':'no data'})

