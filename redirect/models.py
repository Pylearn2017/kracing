from django.db import models

class RoomLink(models.Model):
	link = models.CharField(max_length=50)

	def __str__(self):
		return self.link
