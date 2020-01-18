---
published: true
title: Docker로 MariaDB 설치
categories:
  - Database
date: 2020-01-18T15:00:00.000Z
---

```bash
docker run \
-d \
--restart=always \
--name=mariadb \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=mypassword \
-e TZ=Asia/Seoul \
-v /data/docker/mariadb/conf.d:/etc/mysql/conf.d \
mariadb:latest
```

* -e MYSQL_ROOT_PASSWORD=원하는 비밀번호 (최대 32자리)
* -v /원하는 설정 파일 폴더 경로/conf.d:/etc/mysql/conf.d \