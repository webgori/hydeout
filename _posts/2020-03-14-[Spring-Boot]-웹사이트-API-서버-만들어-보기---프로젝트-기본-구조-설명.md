---
published: true
title: "[Spring Boot] 웹사이트 API 서버 만들어 보기 - 프로젝트 기본 구조 설명"
categories:
  - Spring
date: 2020-03-14T20:41:00.000Z
tags:
  - Spring Boot
---

Spring은 프로젝트 세팅할 때 설정해 줘야 할 게 많은데, 그런 설정들이 자동으로 되어있는 게 Spring Boot이다.

설정 자동화를 제외하고는 Spring과 Spring Boot가 동일하다고 봐도 된다. (엄밀히 따지면 다른 부분도 있겠지만, 쉽게 생각하자)

Spring 프로젝트 구조는 프로젝트마다 다르겠지만, 어느 정도 기본적인 구조는 있다.

프로젝트 구조를 알아야 내가 원하는 것을 어디에 추가하면 되는지 알 수 있다.

lolien-discord-bot 프로젝트로 본 기본적인 프로젝트 파일 구조는 아래와 같다.

```bash
lolien-discord-bot/
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    │   ├── java
    │   │   └── kr
    │   │       └── webgori
    │   │           └── lolien
    │   │               └── discord
    │   │                   └── bot
    │   │                       ├── LolienDiscordBotApplication.java
    │   │                       ├── ServletInitializer.java
    │   │                       ├── controller
    │   │                       │   └── LeagueController.java
    │   │                       ├── entity
    │   │                       │   └── Memo.java
    │   │                       ├── repository
    │   │                       │   └── MemoRepository.java
    │   │                       ├── request
    │   │                       │   └── LeagueAddRequest.java
    │   │                       ├── response
    │   │                       │   └── LeagueGetLeagueResponse.java
    │   │                       └── service
    │   │                           └── LeagueService.java
    │   └── resources
    │       └── application.yml
    └── test
        ├── java
            └── kr
                └── webgori
                    └── lolien
                        └── discord
                            └── bot
                                └── LolienDiscordBotApplicationTests.java
```

## controller
* controller 패키지에는 파일명이 Controller로 끝나는 파일들이 있다.
* URL을 매핑(지정)하고, Service와 연결해 준다.

## service
* service 패키지에는 파일명이 Service로 끝나는 파일들이 있다.
* 비즈니스 로직을 정의하는 곳이다.

## entity (JPA를 사용할 때. 사용하지 않는다면 없다)
* Database의 Table 스키마(구조)를 JAVA로 정의해놓은 클래스라고 보면 된다.

## repository (JPA를 사용할 때. 사용하지 않는다면 없다)
* repository 패키지에는 파일명이 Repository 끝나는 파일들이 있다.
* 이 클래스 파일에 Database 질의(e.g. SELECT * FROM …)를 인터페이스 메서드로 정의해놓는다. (무슨 말인지 아직은 모를 수 있다. 그냥 넘어가자)

## request
* request 패키지에는 파일명이 Request 끝나는 파일들이 있다.
* Client가 API로 보내는 매개변수를 정의해놓는 클래스이다.

## response
* response 패키지에는 파일명이 Response 끝나는 파일들이 있다.
* API 서버가 Client로 보내는 응답을 정의해놓는 클래스이다.