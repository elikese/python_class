# 기존에 만들었던 coord게임을
# class로 분리하고
# 모듈로 정리


# 역할별 설계
"""
콘솔창에 맵을 그리는 역할 -> map class -> map.py모듈
플레이어 이동 -> player class -> player.py 모듈
이동 검증 -> map class
게임 전체 로직담당 -> game class -> game.py 모듈
main에서 각 class 인스턴스 생성, 주입, 호출
"""
