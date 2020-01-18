---
published: true
title: [Linux] root 권한 획득시 비밀번호 입력 안하기
categories:
  - Linux
date: 2020-01-18T12:00:00.000Z
---

```bash
root@nas:~# visudo

#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
webgori ALL=(ALL) NOPASSWD:ALL
```

```
계정명(username) ALL=(ALL) NOPASSWD:ALL 추가
```