#!/usr/bin/env bash
. /opt/PY/bin/activate
start(){
python ./manage.py runfcgi host=127.0.0.1 port=9000 method=prefork maxspare=30 minspare=30 pidfile=/var/run/django_wechat.pid
}
stop(){
kill `cat /var/run/django_wechat.pid`
}
case $1 in
  start)
       start
       echo "django fcgi start done";;
  stop)
       stop
       echo "django fcgi stop done";;
  restart|re)
       stop
       sleep 2
       start
       echo "django fcgi restart done";;
esac