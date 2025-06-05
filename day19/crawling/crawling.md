## HTML이란?
HTML(HyperText Markup Language)은 웹페이지를 만들기 위한 마크업 언어입니다. 
웹브라우저가 이해할 수 있는 구조화된 문서를 만들 때 사용합니다.

## HTML의 기본 구조
```
<html>
<head>
    <title>페이지 제목</title>
</head>
<body>
    <h1>큰 제목</h1>
    <p>본문 내용</p>
</body>
</html>
```
## 주요 구성 요소
- html: HTML 문서의 최상위 요소
- head: 페이지 정보(제목, 스타일 등)를 담는 영역
- body: 실제 페이지 내용이 표시되는 영역

## 크롤링에 중요한 HTML 태그들
1. 제목 태그 (Heading Tags)
```
<h1>가장 큰 제목</h1>
<h2>두 번째 제목</h2>
<h3>세 번째 제목</h3>
-- h6까지 있음 --
```
2. 텍스트 관련 태그
```
<p>문단</p>
<span>인라인 텍스트</span>
<div>블록 요소</div>
<strong>굵은 텍스트</strong>
<em>기울임 텍스트</em>
```
3. 목록 태그
```
<!-- 순서 없는 목록 -->
<ul>
    <li>항목 1</li>
    <li>항목 2</li>
</ul>

<!-- 순서 있는 목록 -->
<ol>
    <li>첫 번째</li>
    <li>두 번째</li>
</ol>
```
4. 링크와 이미지
```
<a href="https://example.com">링크</a>
<img src="image.jpg" alt="이미지 설명">
```
5. 표 (Table)
```
html
<table>
    <thead>
        <tr>
            <th>제목1</th>
            <th>제목2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>데이터1</td>
            <td>데이터2</td>
        </tr>
    </tbody>
</table>
```
## HTML 속성 (Attributes)
속성은 태그의 추가 정보

### 크롤링에서 중요한 속성들
1. id 속성
```html
<div id="main-content">주요 내용</div>
페이지에서 유일한 식별자
CSS나 JavaScript에서 특정 요소를 선택할 때 사용
```

2. class 속성
```html
<p class="highlight">강조된 문단</p>
<div class="card product-item">상품 카드</div>
여러 요소에 같은 클래스를 적용 가능
스타일링이나 요소 선택에 사용
```

## HTML 트리구조
HTML은 트리(Tree) 구조로 되어 있습니다. 각 태그는 노드(node)이고, 부모-자식 관계를 가집니다

## 탐색방법 : 깊이우선탐색(DFS)
1. 현재 노드를 방문
2. 첫 번째 자식으로 이동 (있다면)
3. 자식이 없으면 형제로 이동
4. 형제도 없으면 부모의 다음 형제로 이동