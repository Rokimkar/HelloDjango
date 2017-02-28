import json
import datetime
from django.http import HttpResponse
from django.http import JsonResponse

json_data = open('/Users/snchit/Desktop/Sanchit/work/code/Web/helloworld/helloworld/sample.json')
data = {}
data['Name :'] = 'sanchit' 
data['message'] = 'Hello World!!'
data['url'] = 'http://stackoverflow.com/users/5940309/sanchit-kumar-singh'


json_data.close()
def helloWorld(request):
	return JsonResponse(data)

def current_datetime(request):
	now = datetime.datetime.now()
	html = "ServerTime is %s." %now
	return HttpResponse(html)
