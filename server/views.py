import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def keyboard(request):
    data = {
        'type': 'buttons',
        'buttons': ['배송 예약', '배송 조회 및 기타']
    }

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json; encoding=utf-8')

@csrf_exempt
def message(request):
    #content = request.body.decode('utf-8')['contents']
    #print(content)

    data = {
        'message': {
            'text': '을 선택하셨습니다.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['이전으로 돌아가기']
        }
    }

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json; encoding=utf-8')

def chat_room(request):
    data = {
        'message': {
            'text': 'test'
        }
    }

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json; encoding=utf-8')

def friend(request):
    data = {
        'message': {
            'text': 'test'
        }
    }

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json; encoding=utf-8')
