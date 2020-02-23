---
published: true
title: "[Docker] tomcat 설치"
categories:
  - Spring
date: 2019-09-24T11:08:00.000Z
---
```
docker run -d \
    --name lolien-discord-bot \
    -p 8080:8080 \
    -p 443:443 \
    --restart=always \
    -v /etc/localtime:/etc/localtime:ro \
    -v /usr/local/tomcat/lolien-discord-bot/logs:/usr/local/tomcat/logs \
    -e TZ=Asia/Seoul \
    tomcat:8.5.45-jdk8-adoptopenjdk-hotspot
 
docker cp lolien-discord-bot:/usr/local/tomcat/bin/catalina.sh ./
 
sed -i '2iCATALINA_OPTS="$JAVA_OPTS -Dspring.profiles.active=dev -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 -Dorg.apache.catalina.connector.RECYCLE_FACADES=true -Dorg.apache.catalina.connector.CoyoteAdapter.ALLOW_BACKSLASH=false -Dorg.apache.tomcat.util.buf.UDecoder.ALLOW_ENCODED_SLASH=false -Dorg.apache.coyote.USE_CUSTOM_STATUS_MSG_IN_HEADER=false"' catalina.sh
 
sed -i '3iJAVA_OPTS="$JAVA_OPTS -Djava.security.egd=file:/dev/./urandom"' catalina.sh
 
docker cp catalina.sh lolien-discord-bot:/usr/local/tomcat/bin/catalina.sh
 
docker exec -it lolien-discord-bot find webapps -mindepth 1 -delete
 
docker restart lolien-discord-bot
 
rm -rf catalina.sh
rm -rf server.xml
```