---
published: true
title: [IntelliJ] error unmappable character for encoding MS949
categories:
  - IntelliJ
date: 2020-02-22T23:58:00.000Z
---

## 1. 개요
 * IntelliJ IDEA 2019.2.4에서 테스트 하였습니다.
 * gradle-5.5에서 테스트 하였습니다.
 * 코드에 한글을 입력하고 빌드를 하니 IntelliJ 콘솔에「error: unmappable character for encoding MS949」에러가 나왔습니다.
 
![](/assets/posts/[IntelliJ] error unmappable character for encoding MS949/console.png)
 
## 2. gradle.properties 파일에 옵션 추가
 * 프로젝트 폴더\gradle.properties 파일이 있는지 확인하고 없으면 생성 합니다.
 * gradle.properties 파일에「org.gradle.jvmargs=-Dfile.encoding=UTF-8」옵션을 추가합니다.
 
![](/assets/posts/[IntelliJ] error unmappable character for encoding MS949/projectTree.png)
![](/assets/posts/[IntelliJ] error unmappable character for encoding MS949/gradle.properties.png)

## 3. 빌드
 * 빌드가 에러 없이 진행되는것을 확인할 수 있습니다.