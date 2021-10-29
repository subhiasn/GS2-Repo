from django.shortcuts import render
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def student_create(request):
    if request.method == "POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        print(stream)
        pythondata = JSONParser().parse(stream)
        print(pythondata)
        serializer = StudentSerializer(data=pythondata)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            res={'msg': 'Data Created'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)    
        return HttpResponse(json_data, content_type='application/json')