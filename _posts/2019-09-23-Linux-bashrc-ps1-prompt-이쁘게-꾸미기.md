---
published: true
title: Linux bashrc PS1 이쁘게 꾸미기
categories:
  - Linux
date: 2019-09-23T18:05:00.000Z
---
1. [bashrcgenerator.com] 접속
2. 순서대로 진행 후 4번에 나온 행을 복사 후 /etc/profile에 추가

```
vi /etc/profile

export PS1="[\[$(tput sgr0)\]\[\033[38;5;14m\]\u\[$(tput sgr0)\]\[\033[38;5;15m\]@\[$(tput sgr0)\]\[\033[38;5;11m\]\h\[$(tput sgr0)\]\[\033[38;5;15m\] \[$(tput sgr0)\]\[\033[38;5;219m\]\W\[$(tput sgr0)\]\[\033[38;5;15m\]]\\$ \[$(tput sgr0)\]"

:wq

source /etc/profile
```

[bashrcgenerator.com]: http://bashrcgenerator.com/