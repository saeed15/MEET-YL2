from django.db import models

class poll(models.Model):
	question=models.CharField(max_length = 200)

class answer(models.Model):
	poll = models.ForeignKey(poll)
	awnser = models.CharField(max_length = 200)
	votes = models.IntegerField(default=0)	

# Crhttps://github.com/saeed15/MEET-YL2
