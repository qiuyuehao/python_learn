#!/usr/bin/python3.5
import requests
from fake_useragent import UserAgent
import re
import bs4
from bs4 import BeautifulSoup
import urllib.request as r
import json

url="http://push2.eastmoney.com/api/qt/stock/details/get?ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1,f2,f3,f4&fields2=f51,f52,f53,f54,f55&pos=-11"
def get_dfcfgupiao(stock_num):
	if stock_num == "000001":
		url_addr = url + "&secid=1." + "000001"
	elif stock_num == "399001":
		url_addr = url + "&secid=0." + "399001"
	elif stock_num == "399006":
		url_addr = url + "&secid=0." + "399006"
	elif stock_num.startswith("0"):
		url_addr = url + "&secid=0." + stock_num
	elif stock_num.startswith("3"):
		url_addr = url + "&secid=0." + stock_num
	elif stock_num.startswith("6"):
		url_addr = url + "&secid=1." + stock_num
	else:
		return None
	try:
		print(url_addr)
		r = requests.get(url_addr, headers={
			'User-Agent': UserAgent().random
		}, timeout = 20)
	except requests.exceptions.ConnectionError:
		print('ConnectionError')
		return None
	except requests.exceptions.ChunkedEncodingError:
		print('ChunkedEncodingError')
		return None
	except:
		print('Unfortunitely -- An Unknow Error Happened')
		return None
	r.encoding = r.apparent_encoding
	#print(r.text)
	return r.text
def get_gupiao_info(stock_num):
	html=get_dfcfgupiao(stock_num)
	if html == None:
		return None
	json_data = json.loads(html)

	prePrice = json_data['data']['prePrice']
	details = json_data['data']['details']
	length = len(details)

	#print(json_data['data']['prePrice'])
	#print(len(json_data['data']['details']))
	#print(json_data['data']['details'][len(json_data['data']['details'])-1])
	price = details[length - 1].split(',')[1]
	time = details[length - 1].split(',')[0]
	#print(prePrice, price, time)
	return (prePrice, price, time)
	#soup = BeautifulSoup(html, 'html.parser')
	#result=soup.find("div", attrs={"class":"stock-info","data-spm":"2"})
	#if result == None:
		#return None
	#stock_info=result.find("strong")
	#result_1=result.find("div", attrs={"class":"price s-up "})
	#if result_1 == None:
		#result_1 = result.find("div", attrs={"class":"price s-down "})
	#if result_1 == None:
		#result_1 = result.find("div", attrs={"class":"price s-stop "})
	#if result_1 != None:
		#print(result_1.strong.string)
		#detail_info = result_1.find_all("span")
		#print(detail_info[0].string)
		#print(detail_info[1].string)
		#return (result_1.strong.string, detail_info[0].string, detail_info[1].string)
	
#上证指数https://gupiao.baidu.com/tpl/betsInfo?from=pc&os_ver=1&cuid=xxx&vv=100&format=json&code=sh000001
def get_szzs():
	url_szzs="https://gupiao.baidu.com/tpl/betsInfo?from=pc&os_ver=1&cuid=xxx&vv=100&format=json&code=sh000001"
	response = requests.get(url_szzs, headers={
		'User-Agent': UserAgent().random,
	})
	return response.text
if __name__ == '__main__':
	#szzs_info=get_szzs()
	#szzs_json=json.loads(szzs_info)
	#print(szzs_json['html'])
	#soup_szzs=BeautifulSoup(szzs_json['html'], 'html.parser')
	#print(soup_szzs.find("strong"))
	#html=get_dfcfgupiao("000042")
	#json_data = json.loads(html)
	#print(json_data)
	#print(json_data['data']['prePrice'])
	#print(len(json_data['data']['details']))
	#print(json_data['data']['details'][len(json_data['data']['details'])-1])
	get_gupiao_info("000042")
	#soup = BeautifulSoup(html, 'html.parser')
	#result=soup.find("div", attrs={"class":"stock-info","data-spm":"2"})
	#stock_info=result.find("strong")
	#result=result.find("div", attrs={"class":"price s-up "})
	#if result == None:
		#result = result.find("div", attrs={"class":"price s-down "})
	#if result == None:
		#result = result.find("div", attrs={"class":"price s-stop "})
	#if result != None:
		#print(result.strong.string)
		#detail_info = result.find_all("span")
		#print(detail_info[1].string)
			
