from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name
class Test(models.Model):
	name = models.CharField(max_length=20)
	test = models.CharField(max_length=20)
	add = models.CharField(max_length=20)
	employee = models.ForeignKey("Employee",on_delete=models.CASCADE,related_name='id')

	def __unicode__(self):
		return self.name

