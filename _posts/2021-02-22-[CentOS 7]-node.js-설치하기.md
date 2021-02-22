---
published: true
title: "[CentOS 7] node.js 설치하기"
categories:
  - Linux
date: 2021-02-22T21:58:00.000Z
---

<!--more-->

```console
[admin@nas local]$ vi /home/user/.bashrc
```

```bash
# /home/user/.bashrc 파일에 아래 라인 추가
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

```console
[admin@nas ~]$ source ~/.bashrc
[admin@nas ~]$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 13527  100 13527    0     0  30993      0 --:--:-- --:--:-- --:--:-- 31025
=> Downloading nvm from git to '/home/admin/.nvm'
=> Cloning into '/home/admin/.nvm'...
remote: Enumerating objects: 333, done.
remote: Counting objects: 100% (333/333), done.
remote: Compressing objects: 100% (283/283), done.
remote: Total 333 (delta 38), reused 150 (delta 25), pack-reused 0
Receiving objects: 100% (333/333), 177.15 KiB | 0 bytes/s, done.
Resolving deltas: 100% (38/38), done.
=> Compressing and cleaning up git repository

=> nvm source string already in /home/admin/.bashrc
=> Appending bash_completion source string to /home/admin/.bashrc
=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
[admin@nas ~]$ . ~/.nvm/nvm.sh
[admin@nas ~]$ nvm install 14.15.5
Downloading and installing node v14.15.5...
Downloading https://nodejs.org/dist/v14.15.5/node-v14.15.5-linux-x64.tar.xz...
######################################################################## 100.0%
Computing checksum with sha256sum
Checksums matched!
Now using node v14.15.5 (npm v6.14.11)
Creating default alias: default -> 14.15.5 (-> v14.15.5)

[admin@nas ~]# node -v
v14.15.5
```

* 현재 기준 마지막 LTS 버전인 14.15.5를 설치하였다.
* 마지막 LTS 버전은 [공식 홈페이지][node.js]에서 확인 가능하다.

[node.js]: https://nodejs.org/en/