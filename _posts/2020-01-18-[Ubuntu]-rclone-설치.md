---
published: true
title: "[Ubuntu] rclone 설치"
categories:
  - Linux
date: 2020-01-18T12:05:00.000Z
---

sudo apt install rclone 명령어로 설치시 구버전으로 설치되어 --daemon 옵션이 안먹힌다.

아래 명령어로 최신버전으로 설치하면 사용 가능 하다.

```bash
curl https://rclone.org/install.sh | sudo bash
```