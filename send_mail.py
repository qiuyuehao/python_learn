#!/usr/bin/python3.5
import os
#-*-coding:utf-8-*-

def send_mail_to_myself(title, content):
	cmd = "echo '%s' | mutt -s '%s'  yuqi@synaptics.com" % (content, title)
	print("send mail now cmd:", cmd)
	os.system(cmd)
	
if __name__=='__main__':
	send_mail_to_myself("up up up", "congraduation")