import requests
from .config import API_KEY

_url = 'http://info.sweettracker.co.kr/api/v1/trackingInfo'

_param = {
    't_key': API_KEY,
    't_code': None,
    't_invoice': None
}

_delivery_center = {
    '우체국택배': '01',
    'CJ대한통운': '04',
    '한진택배': '05',
    '로젠택배': '06',
    'KG로지스택배': '07',
    'CU 편의점택배': '46'
}

def _set_delivery_param(code, invoice):
    _param['t_code'] = code
    _param['t_invoice'] = invoice

def _get_delivery_response():
    rsp = requests.get(_url, params=_param).json()
    return rsp

def get_delivery_info(company, invoice):
    code = _delivery_center[company]
    _set_delivery_param(code, invoice)
    info = _get_delivery_response()
    
    try:
        # Checking status == False
        info['status']
        return ('Error', '잘못된 송장번호입니다.')
    
    except KeyError:
        # status != False
        info = info['lastDetail']
        return (info['timeString'], info['kind'])