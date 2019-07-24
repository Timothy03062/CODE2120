from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys
from math import sqrt

@csrf_exempt
def grow(request):
	jsob = {"startNumber": 0, "length": 10, "growthFactor": 1.5, "time": 4} #details
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)
			#custom function 
			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			growthFactor = float(jsob["growthFactor"])
			time = int(jsob["time"])
			loop = range(length)

			numarray = []

			a = startNumber
			b = growthFactor
			x = time 

			for l in loop:
				numarray.append(a)
				a = a * b ** x



			return JsonResponse({"growth":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)