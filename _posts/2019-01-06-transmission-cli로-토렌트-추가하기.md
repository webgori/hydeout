---
published: true
title: transmission cli로 토렌트 추가 및 확인하기
categories:
  - WEB
date: 2019-01-06T11:00:00.000Z
---
```
transmission-remote 9091 -n 'id:password' -a magnet:?xt=urn:btih:dd8255ecdc7ca55fb0bbf81323d87062db1f6d1c&dn=Big+Buck+Bunny&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fbig-buck-bunny.torrent
transmission-remote 9091 -n 'id:password' -a /var/lib/transmission-daemon/downloads/big-buck-bunny.torrent
transmission-remote 9091 -n 'id:password' -a https://webtorrent.io/torrents/big-buck-bunny.torrent
transmission-remote -n 'id:password' --list
```
