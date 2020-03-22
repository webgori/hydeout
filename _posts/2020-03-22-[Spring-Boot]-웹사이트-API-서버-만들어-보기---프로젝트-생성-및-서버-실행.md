---
published: true
title: "[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행"
categories:
  - Spring
date: 2020-03-22T19:45:00.000Z
tags:
  - Spring Boot
---

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321171857.png" data="group" %}

IntelliJ Community 버전은 Spring 기능이 포함되어 있지 않다.

그렇기에 [Spring Initializr] 사이트에서 프로젝트를 생성하고, IntelliJ Community에서 프로젝트를 불러와야 한다.

[Spring Initializr] 사이트에 접속 후 아래 설명을 순서대로 진행한다.

1. Project: Gradle Project
2. Language: Java
3. Spring Boot: 2.2.5 (M3)
4. Project Metadata Group: 회사명, 도메인 주소, 그룹명 등… 개인의 경우 자주 사용하는 아이디를 활용
5. Project Metadata Artifact: 프로젝트명
6. 상세 옵션을 정하기 위해  Options를 클릭
7. Name: Project Metadata Artifact와 동일
8. Description: 프로젝트 설명
9. Package name: Group 명과 Artifact 명을 적절히 혼합하여 사용
10. Packaging: War
11. Java: 11
12. Generate: 적은 것들을 기반으로 프로젝트를 만들어 압축 파일로 다운로드

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321172127.png" data="group" %}

내려받은 압축파일을 압축 해제한다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321162849.png" data="group" %}

설치된 IntelliJ IDEA Community Edition 2019.2.4를 실행한다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321172338.png" data="group" %}

Import Project를 클릭한다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321172426.png" data="group" %}

압축 해제된 폴더를 선택하고 OK 버튼을 누른다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321172516.png" data="group" %}

1. import project from external model 라디오 버튼 선택
2. Gradle 선택 후 Finish 버튼 클릭

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321172607.png" data="group" %}

프로젝트를 불러오고, Gradle을 자동으로 다운받는다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321173130.png" data="group" %}

Gradle 다운로드가 끝나면 Tip 창 왼쪽 하단의 "Show tips on startup"을 체크 해제하고, Close 버튼을 클릭한다.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200321173236.png" data="group" %}

왼쪽에 프로젝트의 파일들이 보일 것이다.

위의 사진처럼 Application으로 끝나는 클래스 파일을 찾아서 마우스 오른쪽 버튼을 누른 후 "Run Application…main()"을 클릭해서 Application을 실행해보자.

{% include lightbox.html src="posts/[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 생성 및 서버 실행/20200322174721.png" data="group" %}

콘솔에 Started Application in…이라고 로그가 나오면 로컬 서버가 실행된 것이다.

[Spring Initializr]: <https://start.spring.io/>