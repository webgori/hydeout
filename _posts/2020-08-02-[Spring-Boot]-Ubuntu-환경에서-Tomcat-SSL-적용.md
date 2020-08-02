---
published: true
title: "[Spring Boot] Ubuntu 환경에서 Tomcat SSL 적용"
categories:
  - Spring
date: 2020-08-02T21:00:00.000Z
tags:
  - Spring Boot
---

<!--more-->

```console
root@nas:~# /usr/local/tomcat/bin/catalina.sh stop
Using CATALINA_BASE:   /usr/local/tomcat
Using CATALINA_HOME:   /usr/local/tomcat
Using CATALINA_TMPDIR: /usr/local/tomcat/temp
Using JRE_HOME:        /usr
Using CLASSPATH:       /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar
NOTE: Picked up JDK_JAVA_OPTIONS:  --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.rmi/sun.rmi.transport=ALL-UNNAMED
root@nas:~# apt-get install certbot
패키지 목록을 읽는 중입니다... 완료
의존성 트리를 만드는 중입니다
상태 정보를 읽는 중입니다... 완료
다음 패키지가 자동으로 설치되었지만 더 이상 필요하지 않습니다:
  fonts-dejavu-extra gir1.2-geocodeglib-1.0 gir1.2-gst-plugins-base-1.0 gir1.2-gudev-1.0 gir1.2-udisks-2.0 grilo-plugins-0.3-base gstreamer1.0-gtk3 libatk-wrapper-java libatk-wrapper-java-jni libcdr-0.1-1
  libcolamd2 libdazzle-1.0-0 libedataserverui-1.2-2 libexiv2-14 libfreerdp-client2-2 libfreerdp2-2 libgc1c2 libgee-0.8-2 libgexiv2-2 libgif7 libglu1-mesa libgom-1.0-0 libgpod-common libgpod4 libice-dev
  liblirc-client0 libllvm8 liblua5.3-0 libmediaart-2.0-0 libmspub-0.1-1 libpthread-stubs0-dev libqqwing2v5 libraw16 libsgutils2-2 libsm-dev libssh-4 libsuitesparseconfig5 libvncclient1 libwinpr2-2
  libx11-dev libx11-doc libxapian30 libxatracker2 libxau-dev libxcb1-dev libxdmcp-dev libxss1 libxt-dev libxvmc1 lp-solve media-player-info python3-mako python3-markupsafe syslinux syslinux-common
  syslinux-legacy usb-creator-common x11-apps x11-session-utils x11proto-core-dev x11proto-dev xbitmaps xinit xorg-sgml-doctools xtrans-dev
Use 'apt autoremove' to remove them.
다음의 추가 패키지가 설치될 것입니다 :
  libpython-stdlib python python-minimal python-pyicu python2.7 python2.7-minimal python3-acme python3-certbot python3-configargparse python3-configobj python3-future python3-josepy python3-mock
  python3-openssl python3-parsedatetime python3-pbr python3-requests-toolbelt python3-zope.component python3-zope.event python3-zope.hookable
제안하는 패키지:
  python3-certbot-apache python3-certbot-nginx python-certbot-doc python-doc python-tk python2.7-doc binfmt-support python-acme-doc python-configobj-doc python-future-doc python-mock-doc
  python-openssl-doc python3-openssl-dbg
다음 새 패키지를 설치할 것입니다:
  certbot libpython-stdlib python python-minimal python-pyicu python2.7 python2.7-minimal python3-acme python3-certbot python3-configargparse python3-configobj python3-future python3-josepy python3-mock
  python3-openssl python3-parsedatetime python3-pbr python3-requests-toolbelt python3-zope.component python3-zope.event python3-zope.hookable
0개 업그레이드, 21개 새로 설치, 0개 제거 및 143개 업그레이드 안 함.
2,852 k바이트 아카이브를 받아야 합니다.
이 작업 후 11.0 M바이트의 디스크 공간을 더 사용하게 됩니다.
계속 하시겠습니까? [Y/n] y
받기:1 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main amd64 python2.7-minimal amd64 2.7.17-1~18.04ubuntu1.1 [1,303 kB]
받기:2 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 python-minimal amd64 2.7.15~rc1-1 [28.1 kB]
받기:3 http://kr.archive.ubuntu.com/ubuntu bionic-updates/main amd64 python2.7 amd64 2.7.17-1~18.04ubuntu1.1 [248 kB]
받기:4 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 libpython-stdlib amd64 2.7.15~rc1-1 [7,620 B]
받기:5 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 python amd64 2.7.15~rc1-1 [140 kB]
받기:6 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 python-pyicu amd64 1.9.8-0ubuntu1 [176 kB]
받기:7 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 python3-openssl all 17.5.0-1ubuntu1 [41.5 kB]
받기:8 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-josepy all 1.1.0-1 [27.6 kB]
받기:9 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 python3-pbr all 3.1.1-3ubuntu3 [53.8 kB]
받기:10 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-mock all 2.0.0-3 [47.5 kB]
받기:11 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-requests-toolbelt all 0.8.0-1 [35.1 kB]
받기:12 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python3-acme all 0.31.0-2~ubuntu18.04.1 [49.3 kB]
받기:13 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-configargparse all 0.11.0-1 [22.4 kB]
받기:14 http://kr.archive.ubuntu.com/ubuntu bionic/main amd64 python3-configobj all 5.0.6-2 [34.2 kB]
받기:15 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-future all 0.15.2-4ubuntu2 [333 kB]
받기:16 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-parsedatetime all 2.4-2 [31.6 kB]
받기:17 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-zope.hookable amd64 4.0.4-4build4 [9,372 B]
받기:18 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-zope.event all 4.2.0-1 [7,402 B]
받기:19 http://kr.archive.ubuntu.com/ubuntu bionic/universe amd64 python3-zope.component all 4.3.0-1 [38.2 kB]
받기:20 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 python3-certbot all 0.27.0-1~ubuntu18.04.1 [201 kB]
받기:21 http://kr.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 certbot all 0.27.0-1~ubuntu18.04.1 [18.2 kB]
내려받기 2,852 k바이트, 소요시간 4초 (811 k바이트/초)
Selecting previously unselected package python2.7-minimal.
(데이터베이스 읽는중 ...현재 210695개의 파일과 디렉터리가 설치되어 있습니다.)
Preparing to unpack .../python2.7-minimal_2.7.17-1~18.04ubuntu1.1_amd64.deb ...
Unpacking python2.7-minimal (2.7.17-1~18.04ubuntu1.1) ...
Selecting previously unselected package python-minimal.
Preparing to unpack .../python-minimal_2.7.15~rc1-1_amd64.deb ...
Unpacking python-minimal (2.7.15~rc1-1) ...
Selecting previously unselected package python2.7.
Preparing to unpack .../python2.7_2.7.17-1~18.04ubuntu1.1_amd64.deb ...
Unpacking python2.7 (2.7.17-1~18.04ubuntu1.1) ...
Selecting previously unselected package libpython-stdlib:amd64.
Preparing to unpack .../libpython-stdlib_2.7.15~rc1-1_amd64.deb ...
Unpacking libpython-stdlib:amd64 (2.7.15~rc1-1) ...
python2.7-minimal (2.7.17-1~18.04ubuntu1.1) 설정하는 중입니다 ...
Linking and byte-compiling packages for runtime python2.7...
python-minimal (2.7.15~rc1-1) 설정하는 중입니다 ...
Selecting previously unselected package python.
(데이터베이스 읽는중 ...현재 210752개의 파일과 디렉터리가 설치되어 있습니다.)
Preparing to unpack .../00-python_2.7.15~rc1-1_amd64.deb ...
Unpacking python (2.7.15~rc1-1) ...
Selecting previously unselected package python-pyicu.
Preparing to unpack .../01-python-pyicu_1.9.8-0ubuntu1_amd64.deb ...
Unpacking python-pyicu (1.9.8-0ubuntu1) ...
Selecting previously unselected package python3-openssl.
Preparing to unpack .../02-python3-openssl_17.5.0-1ubuntu1_all.deb ...
Unpacking python3-openssl (17.5.0-1ubuntu1) ...
Selecting previously unselected package python3-josepy.
Preparing to unpack .../03-python3-josepy_1.1.0-1_all.deb ...
Unpacking python3-josepy (1.1.0-1) ...
Selecting previously unselected package python3-pbr.
Preparing to unpack .../04-python3-pbr_3.1.1-3ubuntu3_all.deb ...
Unpacking python3-pbr (3.1.1-3ubuntu3) ...
Selecting previously unselected package python3-mock.
Preparing to unpack .../05-python3-mock_2.0.0-3_all.deb ...
Unpacking python3-mock (2.0.0-3) ...
Selecting previously unselected package python3-requests-toolbelt.
Preparing to unpack .../06-python3-requests-toolbelt_0.8.0-1_all.deb ...
Unpacking python3-requests-toolbelt (0.8.0-1) ...
Selecting previously unselected package python3-acme.
Preparing to unpack .../07-python3-acme_0.31.0-2~ubuntu18.04.1_all.deb ...
Unpacking python3-acme (0.31.0-2~ubuntu18.04.1) ...
Selecting previously unselected package python3-configargparse.
Preparing to unpack .../08-python3-configargparse_0.11.0-1_all.deb ...
Unpacking python3-configargparse (0.11.0-1) ...
Selecting previously unselected package python3-configobj.
Preparing to unpack .../09-python3-configobj_5.0.6-2_all.deb ...
Unpacking python3-configobj (5.0.6-2) ...
Selecting previously unselected package python3-future.
Preparing to unpack .../10-python3-future_0.15.2-4ubuntu2_all.deb ...
Unpacking python3-future (0.15.2-4ubuntu2) ...
Selecting previously unselected package python3-parsedatetime.
Preparing to unpack .../11-python3-parsedatetime_2.4-2_all.deb ...
Unpacking python3-parsedatetime (2.4-2) ...
Selecting previously unselected package python3-zope.hookable.
Preparing to unpack .../12-python3-zope.hookable_4.0.4-4build4_amd64.deb ...
Unpacking python3-zope.hookable (4.0.4-4build4) ...
Selecting previously unselected package python3-zope.event.
Preparing to unpack .../13-python3-zope.event_4.2.0-1_all.deb ...
Unpacking python3-zope.event (4.2.0-1) ...
Selecting previously unselected package python3-zope.component.
Preparing to unpack .../14-python3-zope.component_4.3.0-1_all.deb ...
Unpacking python3-zope.component (4.3.0-1) ...
Selecting previously unselected package python3-certbot.
Preparing to unpack .../15-python3-certbot_0.27.0-1~ubuntu18.04.1_all.deb ...
Unpacking python3-certbot (0.27.0-1~ubuntu18.04.1) ...
Selecting previously unselected package certbot.
Preparing to unpack .../16-certbot_0.27.0-1~ubuntu18.04.1_all.deb ...
Unpacking certbot (0.27.0-1~ubuntu18.04.1) ...
python3-requests-toolbelt (0.8.0-1) 설정하는 중입니다 ...
python3-pbr (3.1.1-3ubuntu3) 설정하는 중입니다 ...
update-alternatives: using /usr/bin/python3-pbr to provide /usr/bin/pbr (pbr) in auto mode
python3-mock (2.0.0-3) 설정하는 중입니다 ...
python3-zope.event (4.2.0-1) 설정하는 중입니다 ...
python2.7 (2.7.17-1~18.04ubuntu1.1) 설정하는 중입니다 ...
libpython-stdlib:amd64 (2.7.15~rc1-1) 설정하는 중입니다 ...
python3-configargparse (0.11.0-1) 설정하는 중입니다 ...
python3-zope.hookable (4.0.4-4build4) 설정하는 중입니다 ...
python3-future (0.15.2-4ubuntu2) 설정하는 중입니다 ...
update-alternatives: using /usr/bin/python3-futurize to provide /usr/bin/futurize (futurize) in auto mode
update-alternatives: using /usr/bin/python3-pasteurize to provide /usr/bin/pasteurize (pasteurize) in auto mode
python3-openssl (17.5.0-1ubuntu1) 설정하는 중입니다 ...
python3-josepy (1.1.0-1) 설정하는 중입니다 ...
python3-configobj (5.0.6-2) 설정하는 중입니다 ...
python (2.7.15~rc1-1) 설정하는 중입니다 ...
python-pyicu (1.9.8-0ubuntu1) 설정하는 중입니다 ...
python3-acme (0.31.0-2~ubuntu18.04.1) 설정하는 중입니다 ...
python3-parsedatetime (2.4-2) 설정하는 중입니다 ...
python3-zope.component (4.3.0-1) 설정하는 중입니다 ...
python3-certbot (0.27.0-1~ubuntu18.04.1) 설정하는 중입니다 ...
certbot (0.27.0-1~ubuntu18.04.1) 설정하는 중입니다 ...
Created symlink /etc/systemd/system/timers.target.wants/certbot.timer → /lib/systemd/system/certbot.timer.
Processing triggers for desktop-file-utils (0.23-1ubuntu3.18.04.2) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for gnome-menus (3.13.3-11ubuntu1.1) ...
Processing triggers for mime-support (3.60ubuntu1) ...
root@nas:~# certbot certonly --standalone -d lol.kr
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator standalone, Installer None
Enter email address (used for urgent renewal and security notices) (Enter 'c' to
cancel): lol@gmail.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
agree in order to register with the ACME server at
https://acme-v02.api.letsencrypt.org/directory
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(A)gree/(C)ancel: A

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing to share your email address with the Electronic Frontier
Foundation, a founding partner of the Let's Encrypt project and the non-profit
organization that develops Certbot? We'd like to send you email about our work
encrypting the web, EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: N
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for lol.kr
Waiting for verification...
Cleaning up challenges

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/lol.kr/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/lol.kr/privkey.pem
   Your cert will expire on 2020-10-30. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
root@nas:~# vi /usr/local/tomcat/conf/server.xml
```

 1. SSL 적용 전 tomcat 중지
 2. certbot 패키지 설치
 3. certbot certonly --standalone -d 자신의 도메인 명령어로 인증서 발급
 4. tomcat/conf/server.xml 파일 수정

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<!-- Note:  A "Server" is not itself a "Container", so you may not
     define subcomponents such as "Valves" at this level.
     Documentation at /docs/config/server.html
 -->
<Server port="8005" shutdown="SHUTDOWN">
  <Listener className="org.apache.catalina.startup.VersionLoggerListener" />
  <!-- Security listener. Documentation at /docs/config/listeners.html
  <Listener className="org.apache.catalina.security.SecurityListener" />
  -->
  <!--APR library loader. Documentation at /docs/apr.html -->
  <Listener className="org.apache.catalina.core.AprLifecycleListener" SSLEngine="on" />
  <!-- Prevent memory leaks due to use of particular java/javax APIs-->
  <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener" />
  <Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener" />
  <Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener" />

  <!-- Global JNDI resources
       Documentation at /docs/jndi-resources-howto.html
  -->
  <GlobalNamingResources>
    <!-- Editable user database that can also be used by
         UserDatabaseRealm to authenticate users
    -->
    <Resource name="UserDatabase" auth="Container"
              type="org.apache.catalina.UserDatabase"
              description="User database that can be updated and saved"
              factory="org.apache.catalina.users.MemoryUserDatabaseFactory"
              pathname="conf/tomcat-users.xml" />
  </GlobalNamingResources>

  <!-- A "Service" is a collection of one or more "Connectors" that share
       a single "Container" Note:  A "Service" is not itself a "Container",
       so you may not define subcomponents such as "Valves" at this level.
       Documentation at /docs/config/service.html
   -->
  <Service name="Catalina">

    <!--The connectors can use a shared executor, you can define one or more named thread pools-->
    <!--
    <Executor name="tomcatThreadPool" namePrefix="catalina-exec-"
        maxThreads="150" minSpareThreads="4"/>
    -->


    <!-- A "Connector" represents an endpoint by which requests are received
         and responses are returned. Documentation at :
         Java HTTP Connector: /docs/config/http.html
         Java AJP  Connector: /docs/config/ajp.html
         APR (HTTP/AJP) Connector: /docs/apr.html
         Define a non-SSL/TLS HTTP/1.1 Connector on port 8080
    -->
    <!--
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
    -->
    <!-- A "Connector" using the shared thread pool-->
    <!--
    <Connector executor="tomcatThreadPool"
               port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
    -->
    <!-- Define an SSL/TLS HTTP/1.1 Connector on port 8443
         This connector uses the NIO implementation. The default
         SSLImplementation will depend on the presence of the APR/native
         library and the useOpenSSL attribute of the
         AprLifecycleListener.
         Either JSSE or OpenSSL style configuration may be used regardless of
         the SSLImplementation selected. JSSE style configuration is used below.
    -->
    <!--
    <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
               maxThreads="150" SSLEnabled="true">
        <SSLHostConfig>
            <Certificate certificateKeystoreFile="conf/localhost-rsa.jks"
                         type="RSA" />
        </SSLHostConfig>
    </Connector>
    -->

    <Connector port="443" protocol="org.apache.coyote.http11.Http11NioProtocol"
               maxThreads="150" SSLEnabled="true">
        <SSLHostConfig>
            <Certificate certificateFile="/etc/letsencrypt/live/lol.kr/cert.pem"
                         certificateKeyFile="/etc/letsencrypt/live/lol.kr/privkey.pem"
                         certificateChainFile="/etc/letsencrypt/live/lol.kr/chain.pem" />
        </SSLHostConfig>
    </Connector> 

    <!-- Define an SSL/TLS HTTP/1.1 Connector on port 8443 with HTTP/2
         This connector uses the APR/native implementation which always uses
         OpenSSL for TLS.
         Either JSSE or OpenSSL style configuration may be used. OpenSSL style
         configuration is used below.
    -->
    <!--
    <Connector port="8443" protocol="org.apache.coyote.http11.Http11AprProtocol"
               maxThreads="150" SSLEnabled="true" >
        <UpgradeProtocol className="org.apache.coyote.http2.Http2Protocol" />
        <SSLHostConfig>
            <Certificate certificateKeyFile="conf/localhost-rsa-key.pem"
                         certificateFile="conf/localhost-rsa-cert.pem"
                         certificateChainFile="conf/localhost-rsa-chain.pem"
                         type="RSA" />
        </SSLHostConfig>
    </Connector>
    -->

    <!-- Define an AJP 1.3 Connector on port 8009 -->
    <Connector port="8009" protocol="AJP/1.3" redirectPort="8443" />


    <!-- An Engine represents the entry point (within Catalina) that processes
         every request.  The Engine implementation for Tomcat stand alone
         analyzes the HTTP headers included with the request, and passes them
         on to the appropriate Host (virtual host).
         Documentation at /docs/config/engine.html -->

    <!-- You should set jvmRoute to support load-balancing via AJP ie :
    <Engine name="Catalina" defaultHost="localhost" jvmRoute="jvm1">
    -->
    <Engine name="Catalina" defaultHost="localhost">

      <!--For clustering, please take a look at documentation at:
          /docs/cluster-howto.html  (simple how to)
          /docs/config/cluster.html (reference documentation) -->
      <!--
      <Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"/>
      -->

      <!-- Use the LockOutRealm to prevent attempts to guess user passwords
           via a brute-force attack -->
      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <!-- This Realm uses the UserDatabase configured in the global JNDI
             resources under the key "UserDatabase".  Any edits
             that are performed against this UserDatabase are immediately
             available for use by the Realm.  -->
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm"
               resourceName="UserDatabase"/>
      </Realm>

      <Host name="localhost"  appBase="webapps"
            unpackWARs="true" autoDeploy="true">

        <!-- SingleSignOn valve, share authentication between web applications
             Documentation at: /docs/config/valve.html -->
        <!--
        <Valve className="org.apache.catalina.authenticator.SingleSignOn" />
        -->

        <!-- Access log processes all example.
             Documentation at: /docs/config/valve.html
             Note: The pattern used is equivalent to using pattern="common" -->
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="localhost_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />

      </Host>
    </Engine>
  </Service>
</Server>
```

 1. 기본 포트인 8080 주석
 2. 포트를 443으로 설정 및 SSL 인증서 경로 설정 추가
 
```shell
0 4 1 * * /usr/bin/certbot renew --pre-hook="/usr/local/tomcat/bin/catalina.sh stop" --renew-hook="/usr/local/tomcat/bin/catalina.sh start"
```

 * crontab에 매월 1일 인증서 갱신되도록 추가 (갱신 전 tomcat 중지, 갱신 후 tomcat 시작)