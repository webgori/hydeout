---
title: Unable to process Jar entry ...
id: 42
categories:
  - JAVA
date: 2014-06-12 10:46:21
tags:
---

```심각: Unable to process Jar entry [org/apache/ibatis/builder/StaticSqlSource.class] from Jar [jar:file:/C:/Users/user/Documents/workspace-sts-3.5.1.RELEASE/.metadata/.plugins/org.eclipse.wst.server.core/tmp0/wtpwebapps/TEST/WEB-INF/lib/mybatis-3.2.5.jar!/] for annotations java.util.zip.ZipException: invalid LOC header (bad signature) at java.util.zip.ZipFile.read(Native Method) at java.util.zip.ZipFile.access$1400(ZipFile.java:56) at java.util.zip.ZipFile$ZipFileInputStream.read(ZipFile.java:679) at java.util.zip.ZipFile$ZipFileInflaterInputStream.fill(ZipFile.java:415) at java.util.zip.InflaterInputStream.read(InflaterInputStream.java:158) at java.io.BufferedInput```

01\. C:\Users\사용자 계정\.m2 디렉토리 삭제

02\. maven clean

03\. maven update