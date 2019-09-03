#!/usr/bin/python3.5
# -*- coding: utf-8 -*-


import sys, time, threading
import urllib.request
import os, re
import datetime
from send_mail import send_mail_to_myself
from send_wechat_msg import send_wechat_msg_to_myself
message_notify_already = {}
notify_time = 60 * 30
pre_date_day = 0
#  debug = False
debug = False


def compare_notify(name, tmp_str, method):
    global notify_time
    global message_notify_already
    if is_deal_time_now() == False:
        return
    if name in message_notify_already.keys():
        pass
    else:
        message_notify_already[name] = 0
    if message_notify_already[name] == 0:
        #  print("should notify", name, tmp_str)
        new_timer_thread = threading.Timer(notify_time, update_notify_value, (name,)).start()
        message_notify_already[name] = 1
    else:
        method = None
    if method == "wechat":
        send_wechat_msg_to_myself(tmp_str)
    elif method == "mail":
        #  pass
        send_mail_to_myself(tmp_str, "no content")
    else:
        pass
        #print(tmp_str)


def update_notify_when_new_day():
    global pre_date_day
    time_now = time.localtime().tm_mday
    if pre_date_day == 0:
        pre_date_day = time_now
    else:
        if pre_date_day != time_now:
            pre_date_day = time_now
            update_stock_notify()
def update_stock_notify():
    global message_notify_already
    if len(message_notify_already) == 0:
        return
    for kv in message_notify_already:
        message_notify_already[kv] = 1
def is_deal_time_now():
    global debug
    if debug == True:
        return True
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    if now.weekday() == 6:
        return False
    elif now.weekday() == 5:
        return False
    else:
        pass
    time_now = time.localtime()
    if (time_now.tm_hour == 9) and (time_now.tm_min >= 22):
        return True
    if (time_now.tm_hour == 10):
        return True
    if (time_now.tm_hour == 11) and (time_now.tm_min <= 30):
        return True
    if (time_now.tm_hour >= 13) and (time_now.tm_hour < 15):
        return True
    if (time_now.tm_hour == 15) and (time_now.tm_min < 10):
        return True
    return False

def notify_user_message(name, up_down_value, other_info, method):
    global notify_time
    global message_notify_already
    if is_deal_time_now() == False:
        return
    if name in message_notify_already.keys():
        pass
    else:
        message_notify_already[name] = 0
    if message_notify_already[name] == 0:
        print("should notify", name)
        new_timer_thread = threading.Timer(notify_time, update_notify_value, (name,)).start()
        message_notify_already[name] = 1
    else:
        method = None
    if up_down_value > 0:
        tmp_content = name + "good news  上涨了 " + str(up_down_value) + "   other information:" +str(other_info)
    else:
        tmp_content = name + "bad news 下跌了 " + str(up_down_value) + "   other information:" +str(other_info)
    if method == "wechat":
        send_wechat_msg_to_myself(tmp_content)
    elif method == "mail":
        #  pass
        send_mail_to_myself(tmp_content, "no content")
    else:
        pass
        #print(tmp_content)

def update_notify_value(message_id):
    global message_notify_already
    message_notify_already[message_id] = 0
