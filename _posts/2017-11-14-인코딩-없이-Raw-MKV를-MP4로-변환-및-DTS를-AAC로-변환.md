---
title: 인코딩 없이(Raw) MKV를 MP4로 변환 및 DTS를 AAC로 변환
date: 2017-11-14 10:41:52
categories:
  - Data
tags:
---
오픈소스를 사용하여 영상 인코딩 없이 처리합니다.

처리 순서
01. 원본 MKV에서 비디오와 오디오를 분리
02. 오디오 포맷이 DTS일 경우 AAC로 변환
03. 원본 비디오와 변환된 AAC를 MP4 컨테이너로 합침

사용법
01. 변환할 영상을 MKVtoMP4(x64) 폴더 안에 넣는다.
02. MKVtoMP4.cmd 파일을 실행시킨다.
03. 처리된 영상은 MKVtoMP4(x64) 폴더에 있고, 원본 MKV 영상은 originalMKV 폴더에 있다.

크롬캐스트는 DTS를 지원해주지 않기 때문에 AAC로 변환할 경우 유용합니다.

제작자 [skotlex](https://twitter.com/skotlex)님의 허락을 받고 배포합니다.

무단 배포를 금지합니다.

[MKVtoMP4(x64).zip](/assets/posts/인코딩-없이-Raw-MKV를-MP4로-변환-및-DTS를-AAC로-변환/MKVtoMP4(x64).zip)