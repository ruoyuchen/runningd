#! /bin/bash

## 检查当前进程中是否还有celery进程活着
function check() {
    lines=`ps -ef |grep celery | grep ${1} | wc -l`
    if [[ $lines > 0 ]]; then
        echo "${lines}: celery ${1} still running..."
        ps -ef |grep celery | grep ${1}
        return ${lines}
    else
        echo "All celery ${1} has been killed"
        return 0
    fi
}

###  停止所有celery指定进程
function stop() {
    pid=`ps -ef | grep celery | grep ${1} | awk '{if($3 == '1') print $2}'`
    if [[ $pid > 0 ]]; then
        echo "Got ${1} master pid : ${pid}"
        kill $pid
        check $1
        status=$?
        echo "got status....${status}"
        sleep 10s
        until [ $status -eq 0 ]
        do
            check $1
            status=$?
            sleep 5s
        done
    else
        echo "Cannot find master pid for ${1}"
    fi
}


cd /server/metamap/metamap_django

stop worker
stop beat

export C_FORCE_ROOT=true

/server/metamap_virenv/bin/python manage.py celery multi start will -A metamap \
 --pidfile="/var/run/celery/%n.pid" \
  --logfile="/var/log/celery/%n.log" \
  --settings=metamap.config.prod \
  --loglevel=info

tail -20 /var/log/celery/will.log

/server/metamap_virenv/bin/python manage.py celery beat --loglevel=info --logfile="/var/log/celery/beat.log" \
 --pidfile="/var/run/celery/beat.pid" \
 --settings=metamap.config.prod \
 --detach


tail -20 /var/log/celery/beat.log

