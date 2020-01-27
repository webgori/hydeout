---
published: true
title: transmission daemon root 권한으로 실행
categories:
  - Linux
date: 2020-01-27T20:55:00.000Z
---

## 1. 개요
 * Ubuntu 18.04.3 LTS에서 테스트 하였습니다.
 
## 2. transmission-daemon 서비스 정지
```console
root@nas:~# systemctl stop transmission-daemon.service
```

## 3. transmission-daemon 서비스 파일 실행 계정 root로 변경
```console
root@nas:~# vi /etc/init.d/transmission-daemon
```

```shell
... (생략)

NAME=transmission-daemon
DAEMON=/usr/bin/$NAME
USER=debian-transmission
STOP_TIMEOUT=30

export PATH="${PATH:+$PATH:}/sbin"

... (생략)
```

USER=debian-transmission 부분을 USER=root로 변경

```shell
... (생략)

NAME=transmission-daemon
DAEMON=/usr/bin/$NAME
USER=root
STOP_TIMEOUT=30

export PATH="${PATH:+$PATH:}/sbin"

... (생략)
```

## 4. transmission-daemon 시스템 파일 실행 계정 root로 변경
```console
root@nas:~# vi /lib/systemd/system/transmission-daemon.service
```

```ini
[Unit]
Description=Transmission BitTorrent Daemon
After=network.target

[Service]
User=debian-transmission
Type=notify
ExecStart=/usr/bin/transmission-daemon -f --log-error -g /etc/transmission-daemon
ExecStop=/bin/kill -s STOP $MAINPID
ExecReload=/bin/kill -s HUP $MAINPID

[Install]
WantedBy=multi-user.target
```

User=debian-transmission 부분을 User=root로 변경

```ini
[Unit]
Description=Transmission BitTorrent Daemon
After=network.target

[Service]
User=root
Type=notify
ExecStart=/usr/bin/transmission-daemon -f --log-error -g /etc/transmission-daemon
ExecStop=/bin/kill -s STOP $MAINPID
ExecReload=/bin/kill -s HUP $MAINPID

[Install]
WantedBy=multi-user.target
```

## 5. transmission-daemon 실행
```console
root@nas:~# systemctl start transmission-daemon.service
```