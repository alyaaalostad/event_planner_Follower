from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	location=models.CharField(max_length=100)
	date=models.DateField()
	time=models.TimeField()
	seats=models.PositiveIntegerField()
	organizer=models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return "%s - %s" % (self.title, self.location)


	def get_absolute_url(self):
		return reverse('event-details', kwargs={'event_id':self.id})


class UserEvent(models.Model):
	name=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	seats=models.PositiveIntegerField()
	event=models.ForeignKey(Event, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return "%s - %s" % (self.name, self.event.title)

