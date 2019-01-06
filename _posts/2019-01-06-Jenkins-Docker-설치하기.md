---
published: false
title: Jenkins Docker 설치하기
---
```
docker run -d -p 8080:8080 -p 50000:50000 --restart=always --name jenkins jenkins/jenkins:lts
```