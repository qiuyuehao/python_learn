#!/usr/bin/python3.5
import sys, time, threading, os
#-*-coding:utf-8-*-

def send_mail_to_myself(title, content):
    cmd = "echo '%s' | mutt -s '%s'  scutqyh@163.com" % (content, title)
    print("send mail now cmd:", cmd)
    t = threading.Thread(target=os.system,args=(cmd,))
    t.start()
if __name__=='__main__':
    send_mail_to_myself("up up up", "congraduation")
