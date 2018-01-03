from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader,Context
from blog.models import Employee
class Person(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.sex = sex
		self.age = age
	def say(self):
		return "I'm " + self.name

# -*- coding: utf-8 -*-
# Create your views here.
# def index(req):
# 	  context          = {}
#     context['hello'] = 'Hello World!'
#     return render(req, 'index.html', context)
# 	#return HttpResponse('<h1>hello world!!!<h1>')
def index(req):
	user =Person('max',33,'male')
	# user =''
	book_list = [1,2,3,4]
	return render_to_response('index.html',{'book_list':book_list,'user':user})

def dbTest(req):
	# emps = Employee.objects.all()
	# return render_to_response('dbTest.html',{'emps':emps})
	# 添加数据
	# test1 = Employee(name='11111')
	# test1.save()
	#emps = Employee.objects.all()
	# filter相当于SQL中的WHERE，可设置条件过滤结果
	#emps = Employee.objects.filter(id=1,name='cha')
	#-name 排序
	#emps = Employee.objects.order_by('-name')[0:2]
	#emps = Employee.objects.get(id=1)
	# test1 = Employee.objects.get(id=1)
	# test1.name ='iosPhone'
	# test1.save()
	#Employee.objects.filter(id=1).update(name='goodGame')
	#Employee.objects.all().update(name='goodGame')
	#删除即把所有的update 改成delete
	return render_to_response('dbTest.html',{'emps':test1})
	
	

