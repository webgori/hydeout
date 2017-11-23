---
title: 'Linux / Unix: Restart PHP Service Command'
id: 61
categories:
  - PHP
date: 2014-06-23 10:54:00
tags:
---

## Restart PHP by restarting your web-server

Type the following command as per your web-server.

<!--more-->

### Restart <span style="color: #ff9900;">Apache</span> for php service

If you are using Apache web server [type the following command to restart the php](http://www.cyberciti.biz/faq/star-stop-restart-apache2-webserver/):
`# /etc/init.d/apache2 restart`
OR
`# apache2ctl restart`

See [how to restart Apache Web Server on Ubuntu Linux](http://www.cyberciti.biz/faq/ubuntu-linux-start-restart-stop-apache-web-server/) for more information.

### Restart <span style="color: #6666cc;">Nginx</span> for php service

If you are using Nginx web-server [type the following command to restart nginx](http://www.cyberciti.biz/faq/nginx-linux-restart/):
`# /etc/init.d/nginx restart`
OR
`# service nginx restart`
OR
`# nginx -s reload`

### Restart <span style="color: #996633;">Lighttpd</span> for php service

If you are using Lighttpd web-server [type the following command to restart lightpd](http://www.cyberciti.biz/faq/stop-lighttpd-server/):
`# /etc/init.d/lighttpd restart`
OR
`# service lighttpd restart`

## Restart <span style="color: #996633;">PHP-FAM Fastcgi</span> for PHP service

If you are running php via PHP-FAM fastcgi manager, use any one of the following as per your version of Linux/Unix:
`# /etc/init.d/php-fpm restart`
`# /etc/init.d/php5-fpm restart`
OR
`# service php-fpm restart`
OR
`# service php5-fpm restart`
OR
`# restart php-fpm`

출처 : http://www.cyberciti.biz/faq/unix-linux-restart-php-service-command/