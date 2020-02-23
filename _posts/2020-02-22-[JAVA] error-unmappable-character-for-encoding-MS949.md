---
published: true
title: "[JAVA] error: unmappable character for encoding MS949"
categories:
  - JAVA
date: 2020-02-22T23:58:00.000Z
---

## 1. 개요
 * gradle v5.5에서 테스트 하였습니다.
 * 코드에 한글을 입력하고 빌드를 하니「error: unmappable character for encoding MS949」에러가 나왔습니다.
 
{% include lightbox.html src="posts/[JAVA] error unmappable character for encoding MS949/console.png" data="group" %}
 
## 2. 해결 방법

### 2.1. 방법 1 gradle.properties 파일에 옵션 추가
 * 프로젝트 폴더\gradle.properties 파일이 있는지 확인하고 없으면 생성 합니다.
 
 {% include lightbox.html src="posts/[JAVA] error unmappable character for encoding MS949/projectTree.png" data="group" %}
 
 * gradle.properties 파일에 아래의 옵션을 추가합니다.
 
``` properties
org.gradle.jvmargs=-Dfile.encoding=UTF-8
```

{% include lightbox.html src="posts/[JAVA] error unmappable character for encoding MS949/gradle.properties.png" data="group" %}

### 2.2. 방법 2 gradle 버전을 v6.1.1로 변경
 * 프로젝트 폴더\gradle\wrapper\gradle-wrapper.properties 파일의 내용 중 distributionUrl을 아래와 같이 변경합니다.

``` properties
distributionUrl=https\://services.gradle.org/distributions/gradle-6.1.1-all.zip
```

{% include lightbox.html src="posts/[JAVA] error unmappable character for encoding MS949/projectTree2.PNG" data="group" %}
{% include lightbox.html src="posts/[JAVA] error unmappable character for encoding MS949/gradle-wrapper.properties.png" data="group" %}

## 3. 빌드
 * 빌드가 에러 없이 진행되는것을 확인할 수 있습니다.