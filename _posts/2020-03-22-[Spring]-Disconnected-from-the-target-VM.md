---
published: true
title: "[Spring] Disconnected from the target VM, address…"
categories:
  - Spring
date: 2020-03-22T18:02:00.000Z
tags:
  - Spring
---

{% include lightbox.html src="posts/[Spring] Disconnected from the target VM/20200322174417.png" data="group" %}

```
Connected to the target VM, address: '127.0.0.1:14418', transport: 'socket'
OpenJDK 64-Bit Server VM warning: Sharing is only supported for boot loader classes because bootstrap classpath has been appended

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.2.5.RELEASE)

2020-03-22 17:40:47.815  INFO 1476 --- [           main] k.w.d.w.api.DemoWebsiteApiApplication    : Starting DemoWebsiteApiApplication on DESKTOP-NA5N5BP with PID 1476 (C:\Project\demo-website-api\out\production\classes started by webgori in C:\Project\demo-website-api)
2020-03-22 17:40:47.822  INFO 1476 --- [           main] k.w.d.w.api.DemoWebsiteApiApplication    : No active profile set, falling back to default profiles: default
2020-03-22 17:40:49.221  INFO 1476 --- [           main] k.w.d.w.api.DemoWebsiteApiApplication    : Started DemoWebsiteApiApplication in 2.329 seconds (JVM running for 3.782)
Disconnected from the target VM, address: '127.0.0.1:14418', transport: 'socket'

Process finished with exit code 0
```

Spring Application을 실행하니 위와 같은 에러가 났다.

{% include lightbox.html src="posts/[Spring] Disconnected from the target VM/20200322174503.png" data="group" %}

오른쪽 상단의 Application 클래스 명을 클릭하면 드롭 박스가 나오고, Edit Configurations… 메뉴가 나온다.

Edit Configurations… 메뉴를 클릭한다.

{% include lightbox.html src="posts/[Spring] Disconnected from the target VM/20200322174624.png" data="group" %}

Include dependencies with "Provided" scope 옵션을 체크한다.

{% include lightbox.html src="posts/[Spring] Disconnected from the target VM/20200322174557.png" data="group" %}

OK 버튼을 누른다.

{% include lightbox.html src="posts/[Spring] Disconnected from the target VM/20200322174721.png" data="group" %}

Spring Application을 실행하면 잘된다.