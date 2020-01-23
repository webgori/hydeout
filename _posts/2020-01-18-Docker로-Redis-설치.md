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
-v /redis.conf 파일이 있는 폴더 경로:/data \
redis:latest redis-server /data/redis.conf
```

### 설명
1. [redis.conf][redis.conf] 파일 다운로드
2. redis.conf 파일을 원하는 폴더로 이동
3. 위의 docker 명령어 중 "/redis.conf 파일이 있는 폴더 경로"에 redis.conf 파일이 있는 폴더 경로로 수정

[redis.conf]: <http://download.redis.io/redis-stable/redis.conf>