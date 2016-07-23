from django.shortcuts import render, HttpResponse
from django.views.generic import View
# Create your views here.

class tuzona(View):
	def get(self,request):
		#return HttpResponse('Hola Bienvenido')
		return render(request,'hola.html')





#class eeoomm(View):
#	def get(self,resquest):
	#	return HttpResponse('Hola Evolanzer')