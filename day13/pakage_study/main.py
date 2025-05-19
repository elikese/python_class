# 패키지
# 여러개의 파이썬 모듈(py파일)을 묶어놓은 폴더
# 관련된 코드들을 정리해서 그룹화 한 폴더

# __init__.py 파일이 있는 폴더는 패키지로 인식
# 파이썬 구 버전에는 필수, 지금은 필수는 아니지만 권장사항

from a_pakage import a  # print("a에서 출력!")
from b_pakage import b  # print("b에서 출력!")

# a에서 출력!
# b에서 출력!
# import로 해당 모듈을 가져오면,
# 사실상 코드를 복붙해 온 것.

print(__name__)
