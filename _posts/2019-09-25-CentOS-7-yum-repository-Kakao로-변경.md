---
published: true
title: CentOS 7 yum repository Kakao로 변경
categories:
  - Linux
date: 2019-09-25T14:19:00.000Z
---
```bash
> /etc/yum.repos.d/CentOS-Base.repo
 
vi /etc/yum.repos.d/CentOS-Base.repo
 
[base]
name=CentOS-$releasever - Base
baseurl=http://mirror.kakao.com/centos/$releasever/os/$basearch/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
 
#released updates
[updates]
name=CentOS-$releasever - Updates
baseurl=http://mirror.kakao.com/centos/$releasever/updates/$basearch
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
#additional packages that may be useful
 
[extras]
name=CentOS-$releasever - Extras
baseurl=http://mirror.kakao.com/centos/$releasever/extras/$basearch
gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
 
#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus
baseurl=http://mirror.kakao.com/centos/$releasever/centosplus/$basearch
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
 
:wq
 
 
# disable fastestmirror
vi /etc/yum/pluginconf.d/fastestmirror.conf
 
enabled=1 -> enabled=0
 
:wq
```