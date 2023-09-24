#!/bin/sh


#转换成smartdns格式，指定cn组解析
sed "s/^full://g;s/^regexp:.*$//g;s/^/nameserver \//g;s/$/\/cn/g" -i ./cn.conf
