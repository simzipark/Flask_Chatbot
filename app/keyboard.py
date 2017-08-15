class Keyboard:
    """
    메시지에 포함될 키보드의 원시형태들을 가지는 클래스입니다.

    :param list home_buttons: 채팅방 입장시 반환될 버튼들입니다.
    """
    home_buttons = [
        "택배 조회",
        "편의점 택배 예약",
        "기타 설정",
    ]

    company_buttons = [
        '한진택배',
        'CJ대한통운',
        '현대택배',
        '우체국택배',
        '이전으로 돌아가기'
    ]
    
    change_buttons = [
        '시간 변경',
        '장소 변경',
        '이전으로 돌아가기'
    ]