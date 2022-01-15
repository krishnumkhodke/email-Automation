from django.db import models
from django.utils.timezone import now
from . views import sendEmail
# Create your models here.

CITY_CHOICES = (
	('mumbai', 'Mumbai'),
	('delhi', 'Delhi'),
	('chennai', 'Chennai'),
	('bengaluru', 'Banglore'),
	('kolkata', 'Kolkata')
)

class SendNewEmail(models.Model):
	emailAddress = models.EmailField(max_length = 200, null = False)
	name = models.CharField(max_length = 200, null = False)
	city = models.CharField(max_length = 200, choices = CITY_CHOICES, null = False)

	def save(self, *args, **kwargs):
		sendEmail(self.name, self.city, self.emailAddress)
		print("Email sent")
		newEmail = SentEmail(emailAddress = self.emailAddress, name = self.name, city = self.city)
		newEmail.save()

class SentEmail(models.Model):
	emailAddress = models.EmailField(max_length = 200, null = False)
	name = models.CharField(max_length = 200, null = False)
	city = models.CharField(max_length = 200, choices = CITY_CHOICES, null = False)
	time = models.DateTimeField(default = now)

	def __str__(self):
		return self.emailAddress