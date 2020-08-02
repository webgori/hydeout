---
published: true
title: "[Spring Boot] Health Check 추가"
categories:
  - Spring
date: 2020-08-02T20:15:00.000Z
tags:
  - Spring Boot
---

 * 서버의 세부 상태를 확인하려면 Health Check를 사용하면 된다.
 * 설명은 Spring Boot 2.0.9.RELEASE 기준이다.

```gradle
implementation('org.springframework.boot:spring-boot-starter-actuator')
```

 * Health Check 기능은 spring-boot-starter-actuator 라이브러리의 기능 중 하나이므로 사용하려면 actuator 라이브러리를 추가해야한다.
 * spring-boot-starter-actuator 라이브러리는 Spring Boot 버전과 동일한 버전을 사용해야 한다.

```yaml
management:
  endpoints:
    web:
      base-path: /application
      path-mapping:
        health: healthcheck
  endpoint:
    health:
      show-details: always
```

 * base-path: actuator의 base path를 설정한다. (기본값은 /actuator)
 * path-mapping.health: health-check end point (기본값은 health)
 * show-details: health check API에 접근할 때 세부 정보를 확인한다. never, when-authorized, always (기본값은 never)

```json
{"status":"UP"}
```

 * show-details 설정 안했을 때 (기본값 never)

```json
{"status":"UP","details":{"diskSpace":{"status":"UP","details":{"total":234685313024,"free":158591512576,"threshold":10485760}},"redis":{"status":"UP","details":{"version":"5.0.7"}},"db":{"status":"UP","details":{"database":"MariaDB","hello":1}}}}
```

 * show-details always로 설정