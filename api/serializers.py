from rest_framework import serializers
from .models import Student,Customer

class StudentSerializer(serializers.ModelSerializer):

	class Meta():
		model=Student
		fields= ['stuid','name', 'classname', 'rollno' ,'eng', 'maths', 'comp', 'science']

class CustomerSerializer(serializers.ModelSerializer):
	class Meta():
		model=Customer
		fields=['custid','custname','ordervalue']