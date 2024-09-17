### 1. 웹 서버-클라이언트 사이 통신 과정

---

- `HTTP` 규칙에 따라 이뤄짐
1. 사용자(클라이언트)가 웹브라우저에 접속해 URL 입력
2. 사용자 입력한 URL 주소는 사실 **DNS 서비스**에 의해서 설정된 **별칭** → 원래 IP로 변환하여 요청할 서버 확인
3. **서버**에 데이터 **요청** 및 응답 **반환**
4. 서버로부터 받은 응답을 클라이언트에 반환

### 2. 필요한 html 지식

구성
- **HTML** : 웹 페이지 구조를 정의하는 마크업 언어
- **CSS** : HTML 요소를 꾸미는 스타일 시트 언어
- **JavaScript** : 웹 페이지 동작을 제어하는 스크립트 언어

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First HTML Page</title>
</head>
<body>
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
</body>
</html>
```
  - **\<head>** : 문서 정보
  - **\<body>** : 문서 내용
  - **\<html>** : HTML 문서
  - **\<title>** : 문서 제목
```youtube
- https://www.youtube.com/watch?v=0DwfWRh_rPI
```

HTML 요소
```html
<p align="center">Hello, World!</p>
```
- **\<p ~~>** : 시작 태그
- **p** : 태그 이름
- **align** : 속성명
- **center** : 속성값
- **Hello, World!** : 내용
- **\</p>** : 종료 태그


태그 종류
1. **\<h1> ~ \<h6>** : h(head) 태그는 폰트 크기가 다르게 적용되는 제목, h1이 가장 큼
2. **\<p>** : p(paragraph) 태그는 문단을 나타냄 ex) 하나의 
   - \<p>문단\</p>
3. 리스트 (글머리 기호)
   - **\<ul>** : ul(unordered list) 순서 없는 목록
   - **\<ol>** : ol(ordered list) 순서 있는 목록
   - **\<li>** : 목록 항목
4. 테이블
   - **\<table>** : 표
   - **\<tr>** : 행
   - **\<td>** : 셀
   - **\<th>** : 제목 셀
5. 링크, 이미지
   - **\<a>** : 링크, href 속성을 통해 링크 주소 지정
   - **\<img>** : 이미지, src 속성을 통해 이미지 주소 지정
       ```html 
       <!-- example -->
       <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google Logo", width="200", height="100">
       ```
       - width, height 속성을 통해 이미지 크기 조절 가능

6. div
    - **\<div>** : 구획을 나누는 태그
       ```html
       <div style="background-color: lightblue;color: black;padding: 20px;">
           <h3>This is a heading</h3>
           <p>This is a paragraph.</p>
       </div>
       ```
    - **style** 꾸밈, 속성을 통해 배경색 지정 가능

7. 셀렉터 selecter: 특정 요소를 선택하는 방법
    ```html
    <p id="my-paragraph">Hello, World!</p>
    <p class="my-paragraph">Hello, World!</p>
    ``` 
    - **class** : class 속성을 통해 특정 요소 선택
    - **id** : id 속성을 통해 특정 요소 선택, 클래스와 사용방법이 거의 동일하지만, html내에서 단 한번만 사용
    
    body 태그 안에 있는 모든 요소를 선택 해서 css 적용
    ```html
    <!--   -->
    <html>
    <head>
    <style>
    body {background-color: lightblue;}
    h4 {color: navy;}

    </style>
    </head>
    <body>
    ```
    클래스에 style 적용하기
    ```html



99. etc
- **\<form>** : 입력 양식
- **\<input>** : 입력 필드
- **\<button>** : 버튼
- **\<select>** : 드롭다운 목록
- **\<option>** : 드롭다운 목록 항목
- **\<label>** : 입력 필드 레이블
- **\<textarea>** : 여러 줄 입력 필드
- **\<span>** : 텍스트 그룹화
- **\<strong>** : 중요한 텍스트
- **\<em>** : 강조 텍스트
- **\<br>** : 줄 바꿈
- **\<hr>** : 수평선
- **\<meta>** : 메타데이터
- **\<link>** : 외부 리소스 연결

### 3. 크롤링 설계

1. robots.txt: 웹사이트의 크롤링 규칙을 정의하는 파일

```
# https://www.inflearn.com/robots.txt

User-agent: *
Disallow: /carts
Disallow: /orders
Disallow: /course/*/edit
Disallow: /api
Disallow: /assets
Disallow: /auth
Disallow: /oauth2_email_not_validated
Disallow: /email_validation
Disallow: /signout
Disallow: /hello
Disallow: /password
Disallow: /email
Disallow: /admin
Disallow: /course/*/dashboard
# Sitemap: https://www.inflearn.com/sitemap.xml
Sitemap: https://cdn.inflearn.com/sitemaps/sitemap.xml
```
- User-agent: 크롤러의 이름
- Disallow: 크롤러가 접근하지 말아야 할 경로
- Sitemap: 사이트맵 파일의 위치

설계하기: 
- 1단계: 필요한 라이브러리 임포트
- 2단계: 웹 페이지 크롤링 함수 정의
- 3단계: 크롤링할 URL 목록 준비
- 4단계: 메인 함수 정의 및 실행
- 5단계: 실행 및 결과 확인

**1단계: 필요한 라이브러리 임포트**

```python
import asyncio
import aiohttp  # 비동기 HTTP 요청
import aiofiles  # 비동기 파일 I/O (선택 사항)
```

* `asyncio`: 비동기 프로그래밍을 위한 핵심 라이브러리
* `aiohttp`: 비동기 HTTP 요청을 위한 라이브러리
* `aiofiles`: 비동기적으로 파일을 읽고 쓰기 위한 라이브러리 (크롤링한 데이터를 파일에 저장할 때 유용)

**2단계: 웹 페이지 크롤링 함수 정의**

```python
async def crawl_website(url, session, semaphore=None): 
    async with semaphore: # 동시성 제어 (선택 사항)
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    content = await response.text()
                    # ... (1) HTML 파싱 및 데이터 추출 로직 ... 
                    return content
                else:
                    print(f"Error: {response.status} - {url}")
                    return None
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            return None
```

* `async def`: 비동기 함수를 정의합니다.
* `session`: `aiohttp.ClientSession()` 객체를 공유하여 연결을 재사용합니다. 
* `semaphore`: 동시 요청 수를 제한하여 서버 부하를 줄입니다.
* `try...except`: 예외 처리를 통해 오류 발생 시 크롤링이 중단되지 않도록 합니다.
* `(1)`:  Beautiful Soup, lxml 등을 사용하여 HTML을 파싱하고 원하는 데이터를 추출하는 로직을 추가합니다.

**3단계: 크롤링할 URL 목록 준비**

```python
urls = [
    "https://example.com",
    "https://example.com/page2",
    "https://example.com/page3",
    # ... 더 많은 URL 추가 ...
]
```

**4단계: 메인 함수 정의 및 실행**

```python
async def main():
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(5)  # 최대 5개 동시 요청
        tasks = [crawl_website(url, session, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)

        # ... (2) 크롤링한 데이터 처리 로직 ...

if __name__ == "__main__":
    asyncio.run(main())
```

* `async with`: `aiohttp.ClientSession()`을 사용하여 HTTP 연결을 효율적으로 관리합니다. 
* `asyncio.Semaphore`: 동시 요청 수를 제한합니다.
* `asyncio.gather`: 여러 코루틴을 동시에 실행하고 결과를 수집합니다.
* `(2)`:  크롤링한 데이터를 저장, 분석, 또는 다른 작업에 활용하는 로직을 추가합니다.

**5단계:  실행 및 결과 확인**

스크립트를 실행하면, asyncio가 이벤트 루프를 생성하고,  `main()` 함수를 시작합니다.  `main()` 함수는 여러 코루틴을 생성하여 병렬적으로 웹 페이지를 크롤링하고 결과를 처리합니다.

**추가 팁:**

* 로그를 남겨 크롤링 과정을 추적하고 디버깅을 용이하게 합니다.
* 크롤링할 웹사이트의 robots.txt를 확인하고 준수합니다. 
* 사용자 에이전트를 설정하여 봇으로 감지되지 않도록 합니다. 

<br/>
<br/>
<br/>


### 4. POSTMAN?

---

- API 개발, 테스트, 공유 및 문서화하는데 활용되는 API 클라이언트

![image](https://user-images.githubusercontent.com/86637320/234279685-59713411-8d9f-4e01-a634-af255c2cde75.png)

> **Naver 뉴스 검색의 OPEN API**
> 
- Naver 뉴스에 cat을 검색 했을 때 결과 출력 기대 → But 실패

```python
https://openapi.naver.com/v1/search/news?query=cat
```

- `"Not Exist Client ID : Authentication failed. (인증에 실패했습니다.)”` 에러 발생
    - `HEADER`를 통해 Client 정보 추가로 전달해야 함
- 파라미터 → 요청 시 옵션 전달하는 역할
    - display `파라미터` 전달을 통해 검색 결과 개수 50개로 변경

```python
https://openapi.naver.com/v1/search/news?query=cat&display=50
```

### 5. HEADERS 등에 활용되는 SECRET Key 관리하기

---

- `secrets.json` 과 같은 파일에 **정보**를 **저장**하고, 이를 불러오는 별도의 `config.py` 파일 구성하는 것이 좋음

### 6. aiofiles를 활용한 비동기 파일 처리

---

- `aiohttp`을 활용한 비동기 크롤링으로 이미지 `src` 주소를 받아왔다고 가정
- 각 src를 활용해 이미지 저장할 때 `aiofiles`를 활용하면 비동기 파일 처리가 가능함

```python
async def img_downloader(session, img):
    img_name = img.split("/")[-1].split("?")[0]

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)
```