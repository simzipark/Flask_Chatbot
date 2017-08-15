class Keyboard:
    '''
    메시지에 포함될 키보드의 원시형태들을 가지는 클래스입니다.

    :param list home_buttons: 채팅방 입장시 반환될 버튼들입니다.
    '''
    home_buttons = [
        '택배 조회',
        '방문 택배 예약',
        '편의점 택배 예약',
        '기타 설정',
    ]
	
    conv_buttons = [
        'GS25',
        'CU',
        '세븐일레븐',
	]

    company_buttons = [
        '이전으로 돌아가기',
        '한진택배',
        'CJ대한통운',
        '로젠택배',
        '우체국택배',
        'KG로지스택배',
        '롯데택배',
        'KGB택배',
        '대신택배',
        '경동택배',
        'CVSnet 편의점택배',
        'CU 편의점택배',
        'EMS',
        'DHL',
        'UPS',
        'FedEx',
        'TNT Express',
    ]
    
    change_buttons = [
        '시간 변경',
        '장소 변경',
        '이전으로 돌아가기'
    ]
    
    check_buttons = [
        '확인',
        '취소',
    ]