from django.shortcuts import render
import requests
from django.core.mail import send_mail
from xtreme import settings

# Create your views here.
API_KEY = settings.API_KEY

def getTemprature(city):
	response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}').json()
	temp =  (response['main']['temp'] - 273.15)
	result = [temp, '\U0001F603']

	if temp <= 15:
		result[1] = ('\U0001F976')
	elif temp>=25:
		result[1] = ('\U0001F975')
	
	return result

def sendEmail(name, city, email):
	temp = getTemprature(city)
	subject = f'Hi {name}, interested in our services'
	body = f'{temp[0]} Celcius {temp[1]}'
	reciver = [email]
	sender = settings.EMAIL_HOST_USER

	send_mail(subject, body, sender, reciver)
