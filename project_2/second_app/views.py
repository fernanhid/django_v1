from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecord

# Create your views here.

def index(request):
	my_dict = {'insert_me': 'Hello I am from views.py'}

	return render(request, 'second_app/index.html', context = my_dict)


def help(request):
	my_dict = {'insert_help': 'Hello I am from views.py and I am the help page'}

	return render(request, 'second_app/help.html', context = my_dict)


def info(request):
	#my_dict = {'insert_me': 'Hello I am from views.py'}
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {"access_records":webpages_list}

	return render(request, 'second_app/info.html', date_dict)