---
published: true
title: Spring Boot에서 Scheduler 사용하기
categories:
  - Spring
date: 2020-01-16T17:00:00.000Z
---

Spring에서 스케줄러를 사용해야 할 경우 보통은 [Quartz][quartz]를 사용한다.

Spring Boot에서는 자체적으로 스케줄러 기능을 지원하여 사용하기 편하다.

사용법은 아래와 같다.

```java
@EnableScheduling
@SpringBootApplication
public class HomeApplication {
  public static void main(String[] args) {
    SpringApplication.run(HomeApplication.class, args);
  }
}
```

```java
@Service
public class UserService {
  // 1분마다 스케줄링
  @Scheduled(cron = "0 * * ? * *")
  public void logEveryMinute() {
    logger.info("executed");
  }
}
```

@Scheduled 어노테이션은 여러가지 옵션을 제공한다. (아래의 설명은 기본기를 쌓는 [정아마추어 코딩블로그][기본기를 쌓는 정아마추어 코딩블로그]의 내용을 가져왔다.)

1. cron: cron표현식을 지원한다. "초 분 시 일 월 주 (년)"으로 표현한다. cron표현식에 쓸 수 있는 것들(특수문자 활용 포함)이 많은데 해당 내용이 핵심이 아니므로 다른 블로그에서 확인해보기를 바란다. [freeformatter.com][freeformatter] 사이트에서 제공하는 ***Cron expression examples***를 참고하면 좋다.

2. fixedDelay: milliseconds 단위로, 이전 작업이 끝난 시점으로 부터 고정된 시간을 설정한다. ex) fixedDelay = 5000

3. fixedDelayString: fixedDelay와 같은데 property의 value만 문자열로 넣는 것이다. ex) fixedDelay = "5000"

4. fixedRate: milliseconds 단위로, 이전 작업이 수행되기 시작한 시점으로 부터 고정된 시간을 설정한다. ex) fixedRate = 3000

5. fixedRateString: fixedDelay와 같은데 property의 value만 문자열로 넣는 것이다. ex) fixedRate = "3000"

6. initialDelay: 스케줄러에서 메서드가 등록되자마자 수행하는 것이 아닌 초기 지연시간을 설정하는 것이다.

7. initialDelayString: 위와 마찬가지로 문자열로 값을 표현하겠다는 의미다.

8. zone: cron표현식을 사용했을 때 사용할 time zone으로 따로 설정하지 않으면 기본적으로 서버의 time zone이다.

[quartz]: <http://www.quartz-scheduler.org/>
[freeformatter]: <https://www.freeformatter.com/cron-expression-generator-quartz.html>
[기본기를 쌓는 정아마추어 코딩블로그]: <https://jeong-pro.tistory.com/186>