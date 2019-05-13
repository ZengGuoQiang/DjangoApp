from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import re
from server.reptile.eptile import getLink
from server import models
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def getCode(request):
    txt = getLink()
    for value in list(txt):
        value = re.sub('\'', '\"', value)
        print(value)
        # data = json.loads(value)
        models.Link.objects.create(**{'txt':value})
    # return JsonResponse({"result": 0, "msg":eval('u"%s"' % txt)},safe= False)
    return HttpResponse(txt) 
    # return HttpResponse(, content_type='application/json') 
    # res = {
    #     'success': True,
    #     'data':txt
    # }
    # return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')