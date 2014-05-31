#!/bin/sh

#我的iPhone进入wifi后自动启动

IPHONE_MAC="18:af:61:37:67:cf"
ADDRESS="192.168.1.0/24"


#判断手机是否在线,不在线返回空""
check_device()
{
  nmap -sP $1 >/dev/null
  return $(grep $2 /proc/net/arp|wc -l)
}

is_paused()
{
  return $(mpc status|grep "paused"|wc -l)
}

play()
{
  is_paused
  result=$?
  if [ $result -eq 1 ]; then
    echo "被暂停了,不强行播放"
  else
    mpc play
  fi
}

stop()
{
  mpc stop
}

check_device $ADDRESS $IPHONE_MAC
result=$?

if [ $result -eq 1 ]; then
  echo "手机到家了,我们开始吧"
  play
else
  echo "手机不在家,音乐就停止吧"
  stop
fi
