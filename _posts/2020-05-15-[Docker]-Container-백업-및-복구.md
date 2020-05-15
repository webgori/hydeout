---
published: true
title: "[Docker] Container 백업 및 복구"
categories:
  - Docker
date: 2020-05-15T18:10:00.000Z
---

## 1. 백업

```console
[root@localhost ~]# docker ps
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS                  PORTS                                              NAMES
2130dc5d2131        tomcat:latest                                "catalina.sh run"        8 seconds ago       Up 7 seconds            8080/tcp                                           tomcat-container
[root@localhost ~]# docker commit tomcat-container tomcat-backup
sha256:51f35e236c795926d7b1cfc4bf380249df16b681b9b78d6ec09917e35c0a2502
[root@localhost ~]# docker save -o tomcat-container.tar tomcat-backup
```

* container를 커밋하면 image가 생김
* image를 파일로 저장

## 2. 복구

```console
[root@localhost ~]# docker load -i tomcat-container.tar
5f39078cf02c: Loading layer [==================================================>]   47.1kB/47.1kB
Loaded image: tomcat-backup:latest
[root@localhost ~]# docker images
REPOSITORY                       TAG                 IMAGE ID            CREATED             SIZE
tomcat-backup                    latest              51f35e236c79        4 minutes ago       647MB
[root@localhost ~]# docker run -d -p 8080:8080 --restart=always --name tomcat-container tomcat-backup:latest
2ca41281972d0a0568bdbeeba36ed3a219578a234b3a5458f304326e8e7ef303
[root@localhost ~]# docker ps
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS                  PORTS                                              NAMES
2ca41281972d        tomcat-backup:latest                         "catalina.sh run"        4 seconds ago       Up 3 seconds            0.0.0.0:8080->8080/tcp                             tomcat-container
```

* 저장된 image 파일을 docker load 명령어로 불러오기
* run 명령어로 container 추가