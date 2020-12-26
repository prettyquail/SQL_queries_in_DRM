from django.db import models

# Create your models here.
class Student(models.Model):
	stuid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=55,blank=False)
	classname=models.CharField(max_length=55,blank=False)
	rollno=models.IntegerField()
	eng=models.IntegerField(blank=False)
	maths=models.IntegerField(blank=False)
	comp=models.IntegerField(blank=False)
	science=models.IntegerField(blank=False)

class Customer(models.Model):
	cid=models.AutoField(primary_key=True)
	custid=models.IntegerField(blank=False)
	custname=models.CharField(max_length=66)
	ordervalue=models.IntegerField(blank=False)

