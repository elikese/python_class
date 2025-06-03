🧱 HTML이란?
HTML은 웹페이지를 만드는 언어야.
웹 브라우저는 이 HTML 코드를 읽고 우리가 보는 웹사이트 화면으로 바꿔줘.

📦 HTML의 기본 구조
<html>
  <head>
    <title>페이지 제목</title>
  </head>
  <body>
    <h1>큰 제목입니다</h1>
    <p>여기는 단락(paragraph)입니다.</p>
  </body>
</html>


🧩 각 요소 설명
구성요소	설명
<html>	HTML 문서의 시작과 끝
<head>	화면에 보이지 않는 정보 (예: 제목, 스타일 등) # !!! encoding 확인
<title>	브라우저 탭에 뜨는 이름
<body>	화면에 실제로 보이는 모든 것 (제목, 문단, 버튼 등)
<h1> ~ <h6>	제목. 숫자가 작을수록 크고 두껍게 표시됨
<p>	문단 텍스트 (paragraph)
🏷️ HTML 태그(tag)란?
모든 HTML은 태그로 이루어져 있어.
태그는 <이름> 이런 식으로 시작하고, </이름>으로 닫아.

예시:

<p>이건 문단입니다.</p>
<p>: 여는 태그

</p>: 닫는 태그

이건 문단입니다.: 내용

🎨 태그에 속성(attributes)을 줄 수 있어
예시:

<div class="quote">명언이 들어갑니다</div>
<div>: 구역(박스) 역할

class="quote": 이름표 같은 것. 여러 개 중에서 특정한 것만 고를 때 사용

📌 웹 크롤링 시 자주 보는 태그들
태그	역할	예시
<div>	박스(구역) 나누기	<div class="content">내용</div>
<span>	글자 일부 스타일	<span style="color:red">빨강</span>
<a>	링크	<a href="url">링크글</a>
<img>	이미지	<img src="image.jpg">
<p>	문단	<p>내용</p>
<ul> / <li>	리스트 / 항목	<ul><li>1번</li><li>2번</li></ul>
💡 실제 예시
<div class="quote">
  <span class="text">"배우는 것은 빛이다."</span>
  <small class="author">홍길동</small>
</div>
이 HTML에서는

"배우는 것은 빛이다." → <span class="text"> 안에 있음

홍길동 → <small class="author"> 안에 있음

👉 그래서 Python 코드에서 find("span", class_="text") 이런 식으로 찾아가는 거야!


# 부모에서 자식으로 탐색
tr = soup.find("tr", class_="baseList")
td = tr.find("td")  # tr의 자식 중에서
a = td.find("a")    # td의 자식 중에서

# 한 번에 깊은 곳까지
a = tr.find("a", class_="baseList-title")  # tr 안 어디든지

# 형제 관계
em = a.find("em")
next_sibling = em.next_sibling  # em 다음 형제