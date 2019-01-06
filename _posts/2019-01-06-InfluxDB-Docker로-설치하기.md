---
published: true
title: InfluxDB Docker로 설치하기
date: 2019-01-06T13:18:00.000Z
categories:
  - WEB
---
```
docker pull influxdb
docker run -d -p 8086:8086 -p 8083:8083 --name influxdb -e INFLUXDB_ADMIN_ENABLED=true influxdb
```
