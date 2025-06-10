
## BeautifulSoup vs Selenium

```
# BeautifulSoup (정적 크롤링)

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, 'html.parser')
# 페이지가 처음 로드된 HTML만 가져옴
```

```
# Selenium (동적 크롤링)  
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
# 실제 브라우저처럼 JavaScript 실행, 동적 내용 로드
```

**핵심**: BeautifulSoup는 "사진"을 보는 것, Selenium은 "실제 브라우저"를 조작하는 것

## 🤔 언제 Selenium을 써야 하는가?

### BeautifulSoup으로 충분한 경우
- 정적인 HTML 페이지
- 서버에서 완성된 HTML을 바로 제공

### Selenium이 필요한 경우  
- JavaScript로 내용이 동적으로 로드되는 페이지
- 무한 스크롤, 더보기 버튼
- 드롭다운, 팝업 등 사용자 상호작용이 필요한 경우

## 🔍 요소 찾기 방법의 차이

```
# BeautifulSoup
soup.find('div', class_='product-name')
soup.find_all('a', {'href': True})
soup.select('.product .price')
```

```
# Selenium (비슷하지만 다른 문법)
driver.find_element(By.CLASS_NAME, 'product-name')
driver.find_elements(By.TAG_NAME, 'a')
driver.find_elements(By.CSS_SELECTOR, '.product .price')
```

## 📝 텍스트/속성 추출 방법

```
# BeautifulSoup
title = soup.find('h1').text
link = soup.find('a')['href']
```

```
# Selenium (거의 동일)
title = driver.find_element(By.TAG_NAME, 'h1').text
link = driver.find_element(By.TAG_NAME, 'a').get_attribute('href')
```

##  새로운 개념들

### 상호작용 (Interaction)

```python
# BeautifulSoup: 불가능
# 클릭, 스크롤, 입력
# Selenium: 가능
element.click()
element.send_keys("텍스트 입력")
driver.execute_script("window.scrollTo(0, 1000);")
# 특정 요소까지 스크롤
element = driver.find_element(By.ID, "target")
driver.execute_script("arguments[0].scrollIntoView();", element)
```