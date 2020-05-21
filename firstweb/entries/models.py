from django.db import models

class Entry(models.Model):
	text = models.TextField(null=True)
	date_posted = models.DateField(auto_now_add=True)
	
	def __unicode__(self):	
		return self.date_posted

	class Meta:
		ordering = ['-date_posted']
			

class PatientD(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	details = models.TextField(null=True)
	dated = models.DateField(auto_now_add=False)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['-dated']
	
	
