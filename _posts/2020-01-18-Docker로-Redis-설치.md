---
published: true
title: Docker로 Redis 설치
categories:
  - Database
date: 2020-01-18T15:05:00.000Z
---

```bash
docker run \
-d \
--restart=always \
--name=redis \
-p 6379:6379 \
-e TZ=Asia/Seoul \
-v /data/docker/redis/redis.conf:/usr/local/etc/redis/redis.conf \
redis:latest
```

* -v /원하는 설정 파일 폴더 경로/redis.conf:/usr/local/etc/redis/redis.conf \