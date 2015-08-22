#!/usr/bin/env python
#coding=utf-8
server = {}
server['port'] = 7777
server['allow'] = ['127.0.0.1', '211.95.46.182']
server['suggestThreadPoolSize'] = 50

factory = {}
factory['max_connections'] = 50
factory['timeout'] = 3
factory['perdefer'] = 5

SECRET_KEY = '#ioag^zjg!+wq^=x-jum(qz*)*&amp;*h&amp;v@_#@_ks%7l3=dyzqu_t'
