import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def keyboard(request):
    data = {
        'type': 'buttons',
        'buttons': ['1', '2']
    }
    return JsonResponse(json.dumps(data, ensure_ascii=False), safe=False)

@csrf_exempt
def message(request):
    print(request.body)

    data = {
        'message': {
            'text': 'hello world'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['1', '2']
        }
    }

    return JsonResponse(json.dumps(data, ensure_ascii=False), safe=False)