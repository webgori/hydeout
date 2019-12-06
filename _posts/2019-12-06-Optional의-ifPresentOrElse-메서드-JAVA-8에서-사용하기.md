---
published: true
title: Optional의 ifPresentOrElse 메서드 JAVA 8에서 사용하기
categories:
  - Spring
date: 2019-12-06T22:30:00.000Z
---

현재 프로젝트를 JAVA 8로 서비스 중이기 때문에 isPresent() 메서드를 사용하여 false일 때 null 처리를 하였었다.

Optional의 ifPresentOrElse 메서드는 [Java 9에서 추가된 메소드][baeldung]이기 때문에 사용할 수 없었는데, 검색 중 spring-data-commons 라이브러리에서 ifPresentOrElse 메서드를 [지원][spring-data-commons]하는걸 알게되었다!

아래아 같이 사용하면 된다.

``` java
import static org.springframework.data.util.Optionals.ifPresentOrElse;

  @Test
  public void should_PrintUsername_When_FindUser() {
    User user = userRepository.findByUserIdx(1);
    ifPresentOrElse(Optional.ofNullable(user), u -> System.out.println(u.getName()), () -> {
      throw new IllegalArgumentException("invalid user");
    });
  }
```

[baeldung]: <https://www.baeldung.com/java-9-optional>
[spring-data-commons]: <https://docs.spring.io/spring-data/commons/docs/current/api/org/springframework/data/util/Optionals.html#ifPresentOrElse-java.util.Optional-java.util.function.Consumer-java.lang.Runnable->