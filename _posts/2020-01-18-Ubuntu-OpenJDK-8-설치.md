---
published: true
title: Ubuntu OpenJDK 8 설치
categories:
  - Linux
date: 2020-01-18T14:38:00.000Z
---

## 1. 개요
 * Ubuntu 18.04.3 LTS에서 테스트 하였습니다.

## 2. apt로 openjdk-8-jdk 설치
```console
root@nas:~# sudo apt install openjdk-8-jdk
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다
상태 정보를 읽는 중입니다... 완료
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  gir1.2-geocodeglib-1.0 gir1.2-gst-plugins-base-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libcdr-0.1-1 libcolamd2 libdazzle-1.0-0 libedataserverui-1.2-2 libexiv2-14
  libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libglu1-mesa libgom-1.0-0 libgpod-common libgpod4 liblirc-client0 libllvm8 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libqqwing2v5
  libraw16 libsgutils2-2 libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2 libxapian30 libxatracker2 libxss1 libxvmc1 lp-solve media-player-info python3-mako python3-markupsafe syslinux
  syslinux-common syslinux-legacy usb-creator-common x11-apps x11-session-utils xbitmaps xinit
Use 'sudo apt autoremove' to remove them.
제안하는 패키지:
  openjdk-8-demo openjdk-8-source visualvm
다음 새 패키지를 설치할 것입니다:
  openjdk-8-jdk
0개 업그레이드, 1개 새로 설치, 0개 제거 및 22개 업그레이드 안 함.
1,606 k바이트 아카이브를 받아야 합니다.
이 작업 후 1,711 k바이트의 디스크 공간을 더 사용하게 됩니다.
받기:1 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 openjdk-8-jdk amd64 8u242-b08-0ubuntu3~18.04 [1,606 kB]
내려받기 1,606 k바이트, 소요시간 3초 (567 k바이트/초)
Selecting previously unselected package openjdk-8-jdk:amd64.
(데이터베이스 읽는중 ...현재 173515개의 파일과 디렉터리가 설치되어 있습니다.)
Preparing to unpack .../openjdk-8-jdk_8u242-b08-0ubuntu3~18.04_amd64.deb ...
Unpacking openjdk-8-jdk:amd64 (8u242-b08-0ubuntu3~18.04) ...
openjdk-8-jdk:amd64 (8u242-b08-0ubuntu3~18.04) 설정하는 중입니다 ...
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/appletviewer to provide /usr/bin/appletviewer (appletviewer) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jconsole to provide /usr/bin/jconsole (jconsole) in auto mode

```

## 3. 설치 확인
```console
root@nas:~# java -version
openjdk version "1.8.0_242"
OpenJDK Runtime Environment (build 1.8.0_242-8u242-b08-0ubuntu3~18.04-b08)
OpenJDK 64-Bit Server VM (build 25.242-b08, mixed mode)
```