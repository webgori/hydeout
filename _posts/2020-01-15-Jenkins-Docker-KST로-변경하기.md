---
published: true
title: Jenkins Docker KST (대한민국 표준 시간)로 변경하기
categories:
  - Jenkins
date: 2020-01-15T17:00:00.000Z
---

Jenkins를 Docker로 설치할 경우 -e TZ=Asia/Seoul 옵션을 줘서 KST로 맞춘다.

아래의 방법은 위의 방법이 동작하지 않거나, 이미 컨테이너를 만들어버렸을 때 사용할 수 있는 방법이다.

```bash
[root@hostname ~]# docker exec -it jenkins bash
root@5383acd8ee17:/# vi /usr/local/bin/jenkins.sh

exec java "${java_opts_array[@]}" -jar /usr/share/jenkins/jenkins.war "${jenkins_opts_array[@]}" "$@"

22라인의 위 내용을 아래와 같이 변경 해준다.

exec java -Dorg.apache.commons.jelly.tags.fmt.timeZone=Asia/Seoul "${java_opts_array[@]}" -jar /usr/share/jenkins/jenkins.war "${jenkins_opts_array[@]}" "$@"
```