---
title: >-
  15894: Unable to open socket file: target process not responding or HotSpot VM
  not loaded The -F option can be used when the target process is not responding
id: 36
categories:
  - JAVA
date: 2014-05-20 11:10:27
tags:
---

jmap -dump:format=b,file=./dump0.dump 15894

```
15894: Unable to open socket file: target process not responding or HotSpot VM not loaded
The -F option can be used when the target process is not responding
```

CentOS에서 jmap이나 jstack을 사용할 때 위와같은 메시지가 나오면..

아래와같이 해보자.

**sudo -u java유저명** jmap -dump:format=b,file=./dump.dump 15894

Dumping heap to /dump.dump ...
Heap dump file created