---
published: true
title: "[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치"
categories:
  - Spring
date: 2020-03-21T20:00:00.000Z
tags:
  - Spring Boot
---

프로젝트를 개발하려면 자바 개발 키트(Java Development Kit, JDK)가 필요하므로 JDK 11을 설치해보자.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321192119.png" data="group" %}

[AdoptOpenJDK] 사이트에 접속 후 JDK 버전을 OpenJDK 11로 JVM을 HotSpot으로 선택한 후 밑의 Latest release 버튼을 클릭하여 설치 파일을 다운로드한다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193428.png" data="group" %}

다운받은 OpenJDK11U-jdk_x64_windows_hotspot_11.0.6_10.exe 파일을 실행한다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193606.png" data="group" %}

Next 버튼을 누른다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193610.png" data="group" %}

약관 동의 체크 박스에 체크한 후 Next 버튼을 누른다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193645.png" data="group" %}

Next 버튼을 누른다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193648.png" data="group" %}

Install 버튼을 누른다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193708.png" data="group" %}

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193734.png" data="group" %}

설치가 완료되었다.

Finish 버튼을 누른다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193825.png" data="group" %}

JDK 11이 설치되었는지 확인하기 위해서 실행 창(단축키 Window + R)을 열고, cmd를 입력한 후 확인 버튼을 누른다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193835.png" data="group" %}

```
java -version
```

설치된 JAVA의 버전을 확인하기 위해서 위의 명령어를 입력한다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - JDK 11 설치/20200321193837.png" data="group" %}

openjdk version "11.0.6" 이라고 나오므로 설치가 잘 됐다.

[AdoptOpenJDK]: <https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot>