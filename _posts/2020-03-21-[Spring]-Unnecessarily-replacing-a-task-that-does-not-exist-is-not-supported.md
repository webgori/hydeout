---
published: true
title: "[Spring] Unnecessarily replacing a task that does not exist is not supported"
categories:
  - Spring
date: 2020-03-21T22:21:00.000Z
tags:
  - Spring
  - Gradle
---

{% include lightbox.html src="posts/[Spring] Unnecessarily replacing a task that does not exist is not supported/20200321190621.png" data="group" %}

```
Unnecessarily replacing a task that does not exist is not supported.  Use create() or register() directly instead.  You attempted to replace a task named 'DemoWebsiteApiApplication.main()', but there is no existing task with that name.
```

IntelliJ에서 Spring Application을 실행할 때 위와 같은 에러가 나온다면?

{% include lightbox.html src="posts/[Spring] Unnecessarily replacing a task that does not exist is not supported/20200321190754.png" data="group" %}

File - Settings(Ctrl + Alt + S)을 눌러 설정 창을 연다.

{% include lightbox.html src="posts/[Spring] Unnecessarily replacing a task that does not exist is not supported/20200321190854.png" data="group" %}

1. 검색창에 gradle 키워드를 입력한다.
2. 검색 결과에서 Gradle을 선택한다.
3. 오른쪽의 Build and run using과 Run tests using이 Gradle로 되어있으면, 둘 다 IntelliJ IDEA로 변경해 준다.

{% include lightbox.html src="posts/[Spring] Unnecessarily replacing a task that does not exist is not supported/20200321191128.png" data="group" %}

OK 버튼을 누른다.

{% include lightbox.html src="posts/[Spring] Unnecessarily replacing a task that does not exist is not supported/20200322174721.png" data="group" %}

Spring Application을 실행하면 에러가 안 난다.