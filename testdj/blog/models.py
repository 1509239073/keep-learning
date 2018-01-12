from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=20)
	wode = models.CharField(max_length=20,unique = True)

	def __unicode__(self):
		return self.name
class Test(models.Model):
	name = models.CharField(max_length=20)
	test = models.CharField(max_length=20)
	add = models.CharField(max_length=20)
	employee = models.ForeignKey("Employee",on_delete=models.CASCADE,to_field='wode')

	def __unicode__(self):
		return self.name

