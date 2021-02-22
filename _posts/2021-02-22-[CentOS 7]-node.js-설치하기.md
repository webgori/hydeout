---
published: true
title: "[CentOS 7] node.js 설치하기"
categories:
  - Linux
date: 2020-01-17T15:40:00.000Z
---

```console
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash

source ~/.bashrc

nvm install 14.15.5

[admin@nas ~]# node -v
v14.15.5
```

* 현재 기준 마지막 LTS 버전인 14.15.5를 설치하였다.
* 마지막 LTS 버전은 [공식 홈페이지][node.js]에서 확인 가능하다.

[node.js]: https://nodejs.org/en/