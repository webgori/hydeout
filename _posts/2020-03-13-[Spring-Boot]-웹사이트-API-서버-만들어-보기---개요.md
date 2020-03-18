---
published: true
title: "[Spring Boot] 웹사이트 API 서버 만들어 보기 - 개요"
categories:
  - Spring
date: 2020-03-13T21:47:00.000Z
tags:
  - Spring Boot
---

회사에서 Spring Framework로 프로젝트를 진행하고 있다.

팀원 중에 Spring Framework를 사용해본 사람이 나뿐이고, 바쁜 일정으로 세미나를 진행하는 것도 여유롭지 않다.

팀원들이 업무를 진행하면서 Spring Framework 자료를 찾아볼 수 있는 곳이 있으면 좋을 것 같아 **Spring Framework로 웹사이트 API 서버를 만들어 보는 포스팅을 진행해 보려고 한다.**

포스팅을 보면서 모르는 부분은 나에게 바로 물어보면 되니, 좀 더 수월한 업무가 가능하리라 생각된다.

혹시라도 포스팅을 보고 궁금한 점이 있거나, 잘못된 부분이 있으면 Disqus 댓글로 문의 바란다.

아는 범위에서 답변해 주고, 모르면 찾아봐서 알려주고… (찾아도 안 나오면 모르겠…)

## 통합 개발 환경(Integrated Development Environment, IDE)

IntelliJ IDEA Community Edition 2019.2.4 버전을 사용한다.

2019.3 버전도 release 되었는데, QueryDSL 버그가 있어서 안정적인 2019.2.4 버전을 사용한다.

IntelliJ는 최고의 IDE면서 Community Edition은 회사에서도 [무료][IntelliJ 라이선스 나무위키]로 사용 가능하다.

## 자바 개발 키트(Java Development Kit, JDK)

JDK는 라이선스 이슈가 있는데, 오픈소스 라이선스인 AdoptOpenJDK의 [OpenJDK 11 HotSpot]을 사용한다.

## 데이터베이스 서버

데이터베이스 서버 종류가 많은데 우리 회사에서는 Microsoft SQL Server를 사용하고 있다.

이 프로젝트는 회사 팀원들을 위한 것이므로, Microsoft SQL Server를 사용해야 한다.

데이터베이스 관련 설정할 때 MySQL과 MariaDB를 사용하는 방법도 같이 다뤄볼 예정이다.

[IntelliJ 라이선스 나무위키]: <https://namu.wiki/w/IntelliJ%20IDEA#s-2>

[OpenJDK 11 HotSpot]: <https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot>