from datetime import datetime, timedelta

# datetime은 날짜와 시간을 다루는 모듈
# 현재 시간
now = datetime.now()
print("지금:", now)

# 문자열 → datetime
dt = datetime.strptime("2025-05-05 12:30", "%Y-%m-%d %H:%M")
print("변환된 날짜시간:", dt)

# datetime → 문자열
s = now.strftime("%Y년 %m월 %d일 %H시 %M분")
print("포맷된 문자열:", s)

# 날짜 덧셈/뺄셈
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print("내일:", tomorrow)
print("어제:", yesterday)
