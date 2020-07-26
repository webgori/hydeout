---
published: true
title: "[JAVA] JDK 11 Ubuntu에 설치"
categories:
  - JAVA
date: 2020-07-26T16:35:00.000Z
tags:
  - JAVA
---

```console
root@nas:/# java -version
-su: /usr/bin/java: 그런 파일이나 디렉터리가 없습니다
root@nas:/# wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
OK
root@nas:/# sudo add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
기존:1 https://downloads.plex.tv/repo/deb public InRelease
받기:2 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]
기존:3 http://kr.archive.ubuntu.com/ubuntu bionic InRelease
받기:4 https://adoptopenjdk.jfrog.io/adoptopenjdk/deb bionic InRelease [6,155 B]
받기:5 http://kr.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
받기:6 https://adoptopenjdk.jfrog.io/adoptopenjdk/deb bionic/main amd64 Packages [10.9 kB]
받기:7 http://security.ubuntu.com/ubuntu bionic-security/main amd64 DEP-11 Metadata [46.1 kB]
받기:8 http://kr.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]
받기:9 http://security.ubuntu.com/ubuntu bionic-security/universe amd64 DEP-11 Metadata [49.2 kB]
받기:10 http://security.ubuntu.com/ubuntu bionic-security/multiverse amd64 DEP-11 Metadata [2,464 B]
받기:11 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [1,023 kB]
받기:12 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main i386 Packages [719 kB]
받기:13 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main amd64 DEP-11 Metadata [295 kB]
받기:14 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main DEP-11 48x48 Icons [80.2 kB]
받기:15 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1,094 kB]
받기:16 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe i386 Packages [1,026 kB]
받기:17 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 DEP-11 Metadata [279 kB]
받기:18 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe DEP-11 64x64 Icons [462 kB]
받기:19 http://kr.archive.ubuntu.com/ubuntu bionic-updates/multiverse amd64 DEP-11 Metadata [2,468 B]
받기:20 http://kr.archive.ubuntu.com/ubuntu bionic-backports/universe amd64 DEP-11 Metadata [9,288 B]
내려받기 5,356 k바이트, 소요시간 3초 (1,558 k바이트/초)
패키지 목록을 읽는 중입니다... 완료
root@nas:/# sudo apt-get install adoptopenjdk-11-hotspot
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다
상태 정보를 읽는 중입니다... 완료
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  fonts-dejavu-extra gir1.2-geocodeglib-1.0 gir1.2-gst-plugins-base-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libatk-wrapper-java libatk-wrapper-java-jni libcdr-0.1-1
  libcolamd2 libdazzle-1.0-0 libedataserverui-1.2-2 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgif7 libglu1-mesa libgom-1.0-0 libgpod-common libgpod4 libice-dev
  liblirc-client0 libllvm8 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libpthread-stubs0-dev libqqwing2v5 libraw16 libsgutils2-2 libsm-dev libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libx11-dev libx11-doc libxapian30 libxatracker2 libxau-dev libxcb1-dev libxdmcp-dev libxss1 libxt-dev libxvmc1 lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common
  syslinux-legacy usb-creator-common x11-apps x11-session-utils x11proto-core-dev x11proto-dev xbitmaps xinit xorg-sgml-doctools xtrans-dev
Use 'sudo apt autoremove' to remove them.
다음 새 패키지를 설치할 것입니다:
  adoptopenjdk-11-hotspot
0개 업그레이드, 1개 새로 설치, 0개 제거 및 122개 업그레이드 안 함.
194 M바이트 아카이브를 받아야 합니다.
이 작업 후 322 M바이트의 디스크 공간을 더 사용하게 됩니다.
받기:1 https://adoptopenjdk.jfrog.io/adoptopenjdk/deb bionic/main amd64 adoptopenjdk-11-hotspot amd64 11.0.8+10-2 [194 MB]
내려받기 194 M바이트, 소요시간 51초 (3,810 k바이트/초)
Selecting previously unselected package adoptopenjdk-11-hotspot.
(데이터베이스 읽는중 ...현재 210136개의 파일과 디렉터리가 설치되어 있습니다.)
Preparing to unpack .../adoptopenjdk-11-hotspot_11.0.8+10-2_amd64.deb ...
Unpacking adoptopenjdk-11-hotspot (11.0.8+10-2) ...
adoptopenjdk-11-hotspot (11.0.8+10-2) 설정하는 중입니다 ...
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jaotc to provide /usr/bin/jaotc (jaotc) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jar to provide /usr/bin/jar (jar) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jarsigner to provide /usr/bin/jarsigner (jarsigner) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/java to provide /usr/bin/java (java) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/javac to provide /usr/bin/javac (javac) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/javadoc to provide /usr/bin/javadoc (javadoc) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/javap to provide /usr/bin/javap (javap) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jcmd to provide /usr/bin/jcmd (jcmd) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jconsole to provide /usr/bin/jconsole (jconsole) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jdb to provide /usr/bin/jdb (jdb) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jdeprscan to provide /usr/bin/jdeprscan (jdeprscan) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jdeps to provide /usr/bin/jdeps (jdeps) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jhsdb to provide /usr/bin/jhsdb (jhsdb) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jimage to provide /usr/bin/jimage (jimage) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jinfo to provide /usr/bin/jinfo (jinfo) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jjs to provide /usr/bin/jjs (jjs) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jlink to provide /usr/bin/jlink (jlink) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jmap to provide /usr/bin/jmap (jmap) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jmod to provide /usr/bin/jmod (jmod) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jps to provide /usr/bin/jps (jps) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jrunscript to provide /usr/bin/jrunscript (jrunscript) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jshell to provide /usr/bin/jshell (jshell) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jstack to provide /usr/bin/jstack (jstack) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jstat to provide /usr/bin/jstat (jstat) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/jstatd to provide /usr/bin/jstatd (jstatd) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/keytool to provide /usr/bin/keytool (keytool) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/pack200 to provide /usr/bin/pack200 (pack200) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/rmic to provide /usr/bin/rmic (rmic) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/rmid to provide /usr/bin/rmid (rmid) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/rmiregistry to provide /usr/bin/rmiregistry (rmiregistry) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/serialver to provide /usr/bin/serialver (serialver) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/bin/unpack200 to provide /usr/bin/unpack200 (unpack200) in auto mode
update-alternatives: using /usr/lib/jvm/adoptopenjdk-11-hotspot-amd64/lib/jexec to provide /usr/bin/jexec (jexec) in auto mode
root@nas:/# java -version
openjdk version "11.0.8" 2020-07-14
OpenJDK Runtime Environment AdoptOpenJDK (build 11.0.8+10)
OpenJDK 64-Bit Server VM AdoptOpenJDK (build 11.0.8+10, mixed mode)
```