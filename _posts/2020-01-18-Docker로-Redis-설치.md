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


{% highlight console %}
root@nas:~# mkdir -p /etc/redis
root@nas:~# wget http://download.redis.io/redis-stable/redis.conf -O /etc/redis/redis.conf
--2020-01-27 18:56:29--  http://download.redis.io/redis-stable/redis.conf
Resolving download.redis.io (download.redis.io)... 109.74.203.151
접속 download.redis.io (download.redis.io)|109.74.203.151|:80... 접속됨.
HTTP request sent, awaiting response... 200 OK
Length: 61797 (60K) [text/plain]
Saving to: ‘/etc/redis/redis.conf’

/etc/redis/redis.conf                               100%[==================================================================================================================>]  60.35K   106KB/s    in 0.6s

2020-01-27 18:56:30 (106 KB/s) - ‘/etc/redis/redis.conf’ saved [61797/61797]

root@nas:~# ll /etc/redis/redis.conf
-rw-r--r-- 1 root root 61797 11월 20 02:05 /etc/redis/redis.conf
root@nas:~# docker run \
> -d \
> --restart=always \
> --name=redis \
> -p 6379:6379 \
> -e TZ=Asia/Seoul \
> -v /etc/redis:/data \
> redis:latest redis-server /data/redis.conf
Unable to find image 'redis:latest' locally
latest: Pulling from library/redis
8ec398bc0356: Pull complete
da01136793fa: Pull complete
cf1486a2c0b8: Pull complete
a44f7da98d9e: Pull complete
c677fde73875: Pull complete
727f8da63ac2: Pull complete
Digest: sha256:90d44d431229683cadd75274e6fcb22c3e0396d149a8f8b7da9925021ee75c30
Status: Downloaded newer image for redis:latest
35e19c4150f576a8173cb705260b37dab652aebd02a61edaf9f84fbd2b265622
root@nas:~# docker logs redis
1:C 27 Jan 2020 18:56:46.482 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 27 Jan 2020 18:56:46.482 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=1, just started
1:C 27 Jan 2020 18:56:46.482 # Configuration loaded
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 1
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           http://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

1:M 27 Jan 2020 18:56:46.483 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
1:M 27 Jan 2020 18:56:46.483 # Server initialized
1:M 27 Jan 2020 18:56:46.483 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
1:M 27 Jan 2020 18:56:46.483 * Ready to accept connections
root@nas:~#
{% endhighlight %}

```console
root@nas:~# mkdir -p /etc/redis
root@nas:~# wget http://download.redis.io/redis-stable/redis.conf -O /etc/redis/redis.conf
--2020-01-27 18:56:29--  http://download.redis.io/redis-stable/redis.conf
Resolving download.redis.io (download.redis.io)... 109.74.203.151
접속 download.redis.io (download.redis.io)|109.74.203.151|:80... 접속됨.
HTTP request sent, awaiting response... 200 OK
Length: 61797 (60K) [text/plain]
Saving to: ‘/etc/redis/redis.conf’

/etc/redis/redis.conf                               100%[==================================================================================================================>]  60.35K   106KB/s    in 0.6s

2020-01-27 18:56:30 (106 KB/s) - ‘/etc/redis/redis.conf’ saved [61797/61797]

root@nas:~# ll /etc/redis/redis.conf
-rw-r--r-- 1 root root 61797 11월 20 02:05 /etc/redis/redis.conf
root@nas:~# docker run \
> -d \
> --restart=always \
> --name=redis \
> -p 6379:6379 \
> -e TZ=Asia/Seoul \
> -v /etc/redis:/data \
> redis:latest redis-server /data/redis.conf
Unable to find image 'redis:latest' locally
latest: Pulling from library/redis
8ec398bc0356: Pull complete
da01136793fa: Pull complete
cf1486a2c0b8: Pull complete
a44f7da98d9e: Pull complete
c677fde73875: Pull complete
727f8da63ac2: Pull complete
Digest: sha256:90d44d431229683cadd75274e6fcb22c3e0396d149a8f8b7da9925021ee75c30
Status: Downloaded newer image for redis:latest
35e19c4150f576a8173cb705260b37dab652aebd02a61edaf9f84fbd2b265622
root@nas:~# docker logs redis
1:C 27 Jan 2020 18:56:46.482 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 27 Jan 2020 18:56:46.482 # Redis version=5.0.7, bits=64, commit=00000000, modified=0, pid=1, just started
1:C 27 Jan 2020 18:56:46.482 # Configuration loaded
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 5.0.7 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 1
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           http://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

1:M 27 Jan 2020 18:56:46.483 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
1:M 27 Jan 2020 18:56:46.483 # Server initialized
1:M 27 Jan 2020 18:56:46.483 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
1:M 27 Jan 2020 18:56:46.483 * Ready to accept connections
root@nas:~#
```