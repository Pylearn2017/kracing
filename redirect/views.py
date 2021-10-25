from django.shortcuts import render
from django.views.generic import ListView
from .models import RoomLink
# Create your views here.
class RedirectPage(ListView):
	model = RoomLink
	template_name = 'redirect.html'