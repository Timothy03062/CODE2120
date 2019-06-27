from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys
from math import sqrt

@csrf_exempt
def getLength(request):
	jsob = {"side1": 0, "side2": 10} #details
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)
			#custom function 
			side1 = int(jsob["side1"])
			side2 = int(jsob["side2"])

			length = float(input("input"))
			return length 

			side1 = getLength()
			side2 = getLength()

			side3 = sqrt(side1 * side1 + side2 * side2)
			print("the length of your third side is: %.2f" % side3)

			getLength(side1, side2)

			return JsonResponse({"getLength":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)