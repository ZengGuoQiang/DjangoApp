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
        # data = json.loads(value)
        data = models.Link.objects.filter(txt=value)
        for e in data:
            print(e)
            if e != "":
                print(1111)
                # models.Link.objects.create(**{'txt':value})
        # Link.objects.values('value').distinct() .order_by('txt')
    # return JsonResponse({"result": 0, "msg":eval('u"%s"' % txt)},safe= False)
    return HttpResponse(txt)
    # return HttpResponse(, content_type='application/json') 
    # res = {
    #     'success': True,
    #     'data':txt
    # }
    # return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')
def getTxt(request):
    data = serializers.serialize('python', models.Link.objects.all())
    print(data)
    res = {
        'success': True,
        'data':data
    }
    return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')