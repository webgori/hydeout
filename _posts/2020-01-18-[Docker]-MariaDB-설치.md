---
published: true
title: "[Docker] MariaDB 설치"
categories:
  - Database
date: 2020-01-18T15:00:00.000Z
---

## 1. 개요
 * Ubuntu 18.04.3 LTS에서 테스트 하였습니다.
 * MariaDB root 비밀번호는 docker run 명령어 -e MYSQL_ROOT_PASSWORD=원하는 비밀번호 (최대 32자리)를 수정 하시면 됩니다.
 * MariaDB 추가 설정 파일은 docker run 명령어 -v /원하는 설정 파일 폴더 경로/conf.d:/etc/mysql/conf.d \를 수정 하시면 됩니다.

## 2. container 생성
```console
root@nas:~# docker run \
-d \
--restart=always \
--name=mariadb \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=mypassword \
-e TZ=Asia/Seoul \
-v /data/docker/mariadb/conf.d:/etc/mysql/conf.d \
mariadb:latest
412285a374b4b332d2f096a6973af97174a3207656c6af73a7fcc97b1b0f829c
root@nas:~#
```

## 3. 로그 확인
```console
root@nas:~# docker logs mariadbtest
2020-02-15 20:46:28+09:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:10.4.11+maria~bionic started.
2020-02-15 20:46:29+09:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2020-02-15 20:46:29+09:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 1:10.4.11+maria~bionic started.
2020-02-15 20:46:29+09:00 [Note] [Entrypoint]: Initializing database files


PLEASE REMEMBER TO SET A PASSWORD FOR THE MariaDB root USER !
To do so, start the server, then issue the following commands:

'/usr/bin/mysqladmin' -u root password 'new-password'
'/usr/bin/mysqladmin' -u root -h  password 'new-password'

Alternatively you can run:
'/usr/bin/mysql_secure_installation'

which will also give you the option of removing the test
databases and anonymous user created by default.  This is
strongly recommended for production servers.

See the MariaDB Knowledgebase at http://mariadb.com/kb or the
MySQL manual for more instructions.

Please report any problems at http://mariadb.org/jira

The latest information about MariaDB is available at http://mariadb.org/.
You can find additional information about the MySQL part at:
http://dev.mysql.com
Consider joining MariaDB's strong and vibrant community:
https://mariadb.org/get-involved/

2020-02-15 20:46:32+09:00 [Note] [Entrypoint]: Database files initialized
2020-02-15 20:46:32+09:00 [Note] [Entrypoint]: Starting temporary server
2020-02-15 20:46:32+09:00 [Note] [Entrypoint]: Waiting for server startup
2020-02-15 20:46:32 0 [Note] mysqld (mysqld 10.4.11-MariaDB-1:10.4.11+maria~bionic) starting as process 121 ...
2020-02-15 20:46:32 0 [Note] InnoDB: Using Linux native AIO
2020-02-15 20:46:32 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
2020-02-15 20:46:32 0 [Note] InnoDB: Uses event mutexes
2020-02-15 20:46:32 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2020-02-15 20:46:32 0 [Note] InnoDB: Number of pools: 1
2020-02-15 20:46:32 0 [Note] InnoDB: Using SSE2 crc32 instructions
2020-02-15 20:46:32 0 [Note] mysqld: O_TMPFILE is not supported on /tmp (disabling future attempts)
2020-02-15 20:46:32 0 [Note] InnoDB: Initializing buffer pool, total size = 256M, instances = 1, chunk size = 128M
2020-02-15 20:46:32 0 [Note] InnoDB: Completed initialization of buffer pool
2020-02-15 20:46:32 0 [Note] InnoDB: If the mysqld execution user is authorized, page cleaner thread priority can be changed. See the man page of setpriority().
2020-02-15 20:46:32 0 [Note] InnoDB: 128 out of 128 rollback segments are active.
2020-02-15 20:46:32 0 [Note] InnoDB: Creating shared tablespace for temporary tables
2020-02-15 20:46:32 0 [Note] InnoDB: Setting file './ibtmp1' size to 12 MB. Physically writing the file full; Please wait ...
2020-02-15 20:46:32 0 [Note] InnoDB: File './ibtmp1' size is now 12 MB.
2020-02-15 20:46:32 0 [Note] InnoDB: Waiting for purge to start
2020-02-15 20:46:32 0 [Note] InnoDB: 10.4.11 started; log sequence number 60972; transaction id 21
2020-02-15 20:46:32 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
2020-02-15 20:46:32 0 [Note] Plugin 'FEEDBACK' is disabled.
2020-02-15 20:46:32 0 [Warning] 'user' entry 'root@2b710db4f12b' ignored in --skip-name-resolve mode.
2020-02-15 20:46:32 0 [Warning] 'user' entry '@2b710db4f12b' ignored in --skip-name-resolve mode.
2020-02-15 20:46:32 0 [Note] InnoDB: Buffer pool(s) load completed at 200215 20:46:32
2020-02-15 20:46:32 0 [Warning] 'proxies_priv' entry '@% root@2b710db4f12b' ignored in --skip-name-resolve mode.
2020-02-15 20:46:32 0 [Note] Reading of all Master_info entries succeeded
2020-02-15 20:46:32 0 [Note] Added new Master_info '' to hash table
2020-02-15 20:46:32 0 [Note] mysqld: ready for connections.
Version: '10.4.11-MariaDB-1:10.4.11+maria~bionic'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  mariadb.org binary distribution

```

## 4. MariaDB Command-line Client 접속

```console
root@nas:~# docker exec -it mariadb mariadb -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 9
Server version: 10.4.11-MariaDB-1:10.4.11+maria~bionic mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>


```