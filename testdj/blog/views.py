from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader,Context
class Person(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.sex = sex
		self.age = age
	def say(self):
		return "I'm " + self.name


# Create your views here.
# def index(req):
# 	  context          = {}
#     context['hello'] = 'Hello World!'
#     return render(req, 'index.html', context)
# 	#return HttpResponse('<h1>hello world!!!<h1>')
def index(req,id):
	user =Person('max',33,'male')
	# user =''
	book_list = [1,2,3,4]
	return render_to_response('index.html',{'book_list':book_list,'user':user,'id':id})