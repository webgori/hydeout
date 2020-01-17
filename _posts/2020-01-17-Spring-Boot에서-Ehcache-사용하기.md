---
published: true
title: Spring Boot에서 Ehcache 사용하기
categories:
  - Spring
date: 2020-01-17T17:00:00.000Z
---

Spring에서 로컬 캐시가 필요한 경우 Ehcache를 사용하면 편리하다.

```
dependencies {
	implementation('org.springframework.boot:spring-boot-starter-cache')
	
	implementation group: 'javax.cache', name: 'cache-api', version: '1.1.1'
	implementation group: 'org.ehcache', name: 'ehcache', version: '3.8.1'
}
```

```java
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableCaching
public class EhcacheConfig {

}
```

```yaml
spring:
  cache:
    jcache:
      config: classpath:config/ehcache.xml
```

```xml
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="http://www.ehcache.org/v3"
        xmlns:jsr107="http://www.ehcache.org/v3/jsr107"
        xsi:schemaLocation="
            http://www.ehcache.org/v3 http://www.ehcache.org/schema/ehcache-core-3.0.xsd
            http://www.ehcache.org/v3/jsr107 http://www.ehcache.org/schema/ehcache-107-ext-3.0.xsd">

    <cache-template name="template">
        <resources>
            <heap>200</heap>
        </resources>
    </cache-template>

    <cache alias="mainCache" uses-template="template"/>
</config>
```

```java
  @Cacheable(cacheNames = "mainCache", key = "#mainRequest.page")
  public List<MainRanking> mainRanking(MainRequest mainRequest) {
    int page = mainRequest.getPage();
    PageRequest pageRequest = PageRequest.of(page, 10);

    Page<MainRanking> mainRankingPages = mainRepository
        .findByRankingLessThanEqual(10, pageRequest);

    return mainRankingPages.getContent();
  }
```