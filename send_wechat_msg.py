#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from wxpy import *
import requests
from datetime import datetime
import time
#from apscheduler.schedulers.blocking import BlockingScheduler  # 定时框架
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 好友列表
#friendlist = [ensure_one(bot.search(remark_name='father')),
			  #bot.friends().search(remark_name='d')[0],
			  #bot.friends().search(remark_name='申')[:],
			  #bot.friends().search(remark_name='harrison')[0]
			  #]
#print(friendlist)


def get_weather(location):
	# 准备url地址，得出location的结果
	path = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=nfYh85yMWI95GUC8HF73sTITmymoWFWq&callback=?'
	url = path % location
	response = requests.get(url)
	result = response.json()
	print(result)
	str1 = '    你的城市: %s\n' % location
	
	# 如果城市错误就按照成都的结果
	if result['error'] != 0:
		str1 = '    你的地区%s获取失败，请修改资料。默认参数：深圳\n' % location
		location = '深圳'
		url = path % location
		response = requests.get(url)
		result = response.json()

	str0 = ('    这是明天的天气预报！送给狡猾的老妖精\n')
	results = result['results']
	# 取出数据字典
	data1 = results[0]
	# 取出pm2.5值
	pm25 = data1['pm25']
	str2 = '    PM2.5 : %s  ' % pm25
	# 将字符串转换为整数 否则无法比较大小
	pm25 = int(pm25)
	if pm25 == '':
		pm25 = 0
	# 通过pm2.5的值大小判断污染指数
	if 0 <= pm25 < 35:
		pollution = '优'
	elif 35 <= pm25 < 75:
		pollution = '良'
	elif 75 <= pm25 < 115:
		pollution = '轻度污染'
	elif 115 <= pm25 < 150:
		pollution = '中度污染'
	elif 150 <= pm25 < 250:
		pollution = '重度污染'
	elif pm25 >= 250:
		pollution = '严重污染'
	str3 = '    空气指数: %s\n' % pollution
	result1 = results[0]
	weather_data = result1['weather_data']
	data = weather_data[1]
	datetime = data['date']
	temperature = data['temperature']
	str4 = '    明天温度: %s%s\n' % (datetime, temperature)
	wind = data['wind']
	str5 = '    风向 : %s\n' % wind
	weather = data['weather']
	str6 = '    天气 : %s\n' % weather
 #  str7 ='    温度 : %s\n' % data['temperature']
	message = data1['index']
	str8 = '    穿衣 : %s\n' % message[0]['des']
	#str9 ='    我很贴心: %s\n' % message[2]['des']
	#str10 ='    运动 : %s\n' % message[3]['des']
	str11 = '    紫外线 : %s\n' % message[4]['des']
	#str12="\n   请注意身体~\n"
	str = str0 + str1 + str2 + str3 + str4 + str5 + str6 + str8 + str11
	print(str)
	return str


def get_iciba():
	url = "http://open.iciba.com/dsapi/"
	r = requests.get(url)
	content = r.json()['content']
	note = r.json()['note']
	str = '    每日一句：\n' + content + '\n' + note + '\n'
	return str

# 发送函数


def send_message():
	for i in range(len(friendlist)):
		friend = friendlist[i]
		location = friend.city
		print(i + 1, '/%s' % len(friendlist), ' 姓名：%s' %
			  friend, ' 地区：%s' % location)
		text = get_weather(friend.city) + get_iciba() + '    好梦~'
		friend.send(text)
		# 发送成功通知我
		bot.file_helper.send(friend)
		bot.file_helper.send('发送完毕')
	return
def send_message_to_onefriend():
		location = friend.city
		print(' 姓名：%s' %
			  friend, ' 地区：%s' % location)
		text = get_weather("深圳龙岗") + get_iciba() + '    小心心送给你~'
		friend.send(text)
		# 发送成功通知我
		#bot.file_helper.send(friend)
		bot.file_helper.send('发送完毕')
		return
def send_wechat_msg_to_myself(text):
		#location = friend.city
		#print(' 姓名：%s' %
			  #friend, ' 地区：%s' % location)
		#text = get_weather("深圳龙岗") + get_iciba() + '    小心心送给你~'
		#print("call send_wechat_msg_to_myself")
		friend.send(text)
		#print("call send_wechat_msg_to_myself  2")
		# 发送成功通知我
		#bot.file_helper.send(friend)
		#bot.file_helper.send('发送完毕')
		return
# 执行程序时直接发送
# send_message()
#  bot = Bot(cache_path=True)  # 登陆微信
#  #tuling = Tuling(api_key='ee161831f6d04cef91a27a7f08beb0c6')  # 机器人api
		#  # 单个好友
		#  # friend = bot.friends().search('harrison')[0]#好友的微信昵称，或者你存取的备注
		#  #location = friend.city
		#  # print(friend)
		#  # print(friend.city)
		#  # 单个好友
#  friend = bot.friends().search('我的小助手')[0]#好友的微信昵称，或者你存取的备注
#  location = friend.city
#  print(friend)
#  print(friend.city)

#  # 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
#  @bot.register(bot.self, except_self=False)
#  def reply_self(msg):
	#  return 'received: {} ({})'.format(msg.text, msg.type)

#  my_friend = ensure_one(bot.search('无双'))
#  #tuling = Tuling(api_key='你申请的 API KEY')

#  # 使用图灵机器人自动与指定好友聊天
#  @bot.register(my_friend)
#  def reply_my_friend(msg):
    #  tuling.do_reply(msg)

#  # 定时器
#  #print('start')
#  #send_message_to_onefriend()
#  #sched = BlockingScheduler()
#  #sched.add_job(send_message, 'cron', day_of_week='0-6',
#  #			  hour=23, minute=00)  # 设定发送的时间
#  #sched.start()
