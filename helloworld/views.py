import json
from django.http import HttpResponse
from django.http import JsonResponse

json_data = open('/Users/snchit/Desktop/Sanchit/work/code/Web/helloworld/helloworld/sample.json')
data = {}
data['Name :'] = 'sanchit' 
data['message'] = 'Hello World!!'

json_data.close()
def helloWorld(request):
	return JsonResponse(data)