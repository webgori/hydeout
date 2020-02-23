---
published: true
title: "[Jekyll] Lightbox 적용"
categories:
  - WEB
date: 2020-02-23T16:30:00.000Z
tags:
  - Jekyll
---

## 1. 개요
 * 블로그에 사진을 올리니 작게 나와 Lightbox를 적용하게 되었습니다.
 * 구글링을 하다가 해당 [사이트][googling]를 발견 하였고, 한글로 내용을 정리 합니다.
 
## 2. Lightbox Github에서 파일 다운로드
 * Lightbox [Github]에서 Source code (zip) 파일을 다운로드 합니다.
 
 {% include lightbox.html src="posts/[Jekyll] Lightbox 적용/lightboxDownload.png" data="group" %}

## 3. 다운로드 받은 파일 assets 폴더로 이동
 1. \assets\css, \assets\js, \assets\images 경로에 폴더가 있는지 확인하고, 없으면 폴더를 만듭니다.
 
 {% include lightbox.html src="posts/[Jekyll] Lightbox 적용/makeFolders.png" data="group" %}
 
 2. 다운받은 파일을 압축 해제 후 \dist\css\lightbox.min.css, \dist\js\lightbox-plus-jquery.min.js, \dist\images\close.png, \dist\images\loading.png, \dist\images\next.png, \dist\images\prev.png 파일들을 1번에서 만든 각각의 폴더로 복사합니다.
 
## 4. Lightbox 스크립트 적용
 * \_includes\head.html 파일에 아래 내용을 추가 합니다.
 
 ``` html
  <!-- CSS -->
  <link rel="stylesheet" href="{{ site.baseurl }}/assets/css/lightbox.min.css">
  
  <!-- Script -->
  <script type="text/javascript" src="{{ site.baseurl }}/assets/js/lightbox-plus-jquery.min.js"></script>
  
  <script>
    lightbox.option({
      'resizeDuration': 200,
      'wrapAround': true
    })
  </script>
 ```

## 5. lightbox.html 파일 추가
 1. \_includes\lightbox.html 파일을 아래 내용으로 추가합니다.
 
 ``` plaintext
 <a href="{{ site.github.url }}/assets/{{ include.src }}" data-lightbox="{{ include.data }}" data-title="{{ include.title }}"><img src="{{ site.github.url }}/assets/{{ include.src }}" alt="{{ include.title }}" width="{{ include.width }}"/></a>
 ```
 
 ```plaintext
 <a href="{{ site.github.url }}/assets/{{ include.src }}" data-lightbox="{{ include.data }}" data-title="{{ include.title }}"><img src="{{ site.github.url }}/assets/{{ include.src }}" alt="{{ include.title }}" width="{{ include.width }}"/></a>
 ```
 
 ```
 <a href="{{ site.github.url }}/assets/{{ include.src }}" data-lightbox="{{ include.data }}" data-title="{{ include.title }}"><img src="{{ site.github.url }}/assets/{{ include.src }}" alt="{{ include.title }}" width="{{ include.width }}"/></a>
 ```

## 6. 이미지 삽입 (사용법)
 
### 6.1. 일반 이미지 삽입
 {% include lightbox.html src="images/lightbox-sample.jpg" data="group" %}
  
 ``` liquid
 {% raw %}
 {% include lightbox.html src="images/lightbox-sample.jpg" data="group" %}
 {% endraw %}
 ```

### 6.2. width 조절 이미지 삽입
 {% include lightbox.html src="images/lightbox-sample.jpg" data="group" width="200px" %}
  
 {% raw %}
 {% include lightbox.html src="images/lightbox-sample.jpg" data="group" width="200px" %}
 {% endraw %}
 
[googling]: <https://blog.aldomann.com/using-lightbox/>
[Github]: <https://github.com/lokesh/lightbox2/releases>