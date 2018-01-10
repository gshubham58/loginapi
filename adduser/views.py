from django.shortcuts import render
from django.http import HttpResponse
from .models import Detail
from rest_framework.response import Response
from .serializer import DetailSerializer
from rest_framework.views import APIView

# Create your views here.
def index(request):
    return HttpResponse("Welcome")
def add(request,ud,pd):
    a=Detail(username=ud,password=pd)
    a.save()
    return HttpResponse("details given are "+str(ud)+" "+str(pd))
class list(APIView):
    def get(self,request):
        De=Detail.objects.all()
        serial=DetailSerializer(De,many=True)
        return Response(serial.data)

