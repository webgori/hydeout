---
published: true
title: "[Docker] Jenkins JDK8 설치"
categories:
  - Jenkins
date: 2019-09-23T17:36:00.000Z
---
```console
root@nas:/data/docker# docker run \
     -d \
     --name jenkins \
     --restart=always \
     -p 8080:8080 \
     -p 50000:50000 \
     -v /etc/localtime:/etc/localtime:ro \
     -v /var/jenkins_home:/var/jenkins_home \
     -u 0 \
     -e TZ=Asia/Seoul \
     jenkins
Unable to find image 'jenkins' locally
jdk11: Pulling from jenkins/jenkins
3192219afd04: Pull complete
17c160265e75: Pull complete
cc4fe40d0e61: Pull complete
9d647f502a07: Pull complete
d108b8c498aa: Pull complete
9c9d47e69698: Pull complete
8600203e8c30: Pull complete
9036ad02413a: Pull complete
31a7dfa0017a: Pull complete
c1bfd26ca733: Pull complete
ef77a0e9029e: Pull complete
4e0ad2cf13cb: Pull complete
41a32805076a: Pull complete
5a4e37182204: Pull complete
8acb0d678637: Pull complete
fdb08974fb79: Pull complete
fd9d86c56caa: Pull complete
533bec90e8a4: Pull complete
2a3d060ab316: Pull complete
Digest: sha256:c037569d014fabab45ce7da03951de88930b91926a7c15a7adec6b7f8dfba6d2
Status: Downloaded newer image for jenkins
f102b2a79d2fd58cadb936306234aa26665b4be3ad9f194493b965294a786137
```