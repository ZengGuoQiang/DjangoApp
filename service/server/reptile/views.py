from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from server.reptile.eptile import getLink
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def getCode(request):
    txt = getLink()
    # return JsonResponse({"result": 0, "msg":eval('u"%s"' % txt)},safe= False)
    
    return HttpResponse(txt) 
    # return HttpResponse(, content_type='application/json') 
    # res = {
    #     'success': True,
    #     'data':txt
    # }
    # return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')