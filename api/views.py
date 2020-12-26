from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db.models import Sum
from rest_framework.parsers import  JSONParser
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializer,CustomerSerializer
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import *
# Create your views here.


@api_view(['GET'])
def selectall(request):

	cols = Student.objects.values('stuid','name','classname','rollno','eng','maths','comp','science')
	count=0
	for i in cols.values('name').distinct():
		count=count+1
	print(count)
	serializer = StudentSerializer(cols, many=True)
	col=[]

	for field in Student._meta.fields:
		col.append(field.name)
		
	
	msg={'column':col,'data':cols.values_list('stuid','name','classname','rollno','eng','maths','comp','science'),'length':count}
	return Response(msg,status=HTTP_200_OK)

@api_view(['GET'])
def selected(request):
	cols=Student.objects.values('name','maths')
	count=0
	for i in cols.values('maths').distinct():
		count=count+1
	serializer=StudentSerializer(cols,many=True)

	col=[]
	for field in cols:
		col.append(field.keys())
	msg={'column':col[0],'data':cols.values_list('name','maths'),'length':count}
	return Response(msg,status=HTTP_200_OK)

@api_view(['GET'])
def aggregate(request):
	cols=Customer.objects.values('custname','ordervalue')
	count=0
	
	for i in cols.values('custname').distinct():
		count=count+1
	
	result = Customer.objects.values('custname').order_by('custname').annotate(totalsum_price=Sum('ordervalue'))
	temp=[]
	for field in result.values('custname','totalsum_price'):
		temp.append(field.values())
	
	serializer=CustomerSerializer(cols,many=True)
	col=[]
	print(temp)
	for field in cols:
		col.append(field.keys())
	msg={'columns':col[0],'data':temp,'length':count}
	return Response(msg,status=HTTP_200_OK)
