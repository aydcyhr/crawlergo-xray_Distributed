#!/usr/bin/python3
# coding: utf-8
import simplejson
import threading
import subprocess
import requests
import warnings
import json
import os


warnings.filterwarnings(action='ignore')

def main(data1,n):
	target = data1
	json = str(n)+'.json'
	print(json)
	cmd = ["crawlergo.exe", "-c", "C:\Program Files\Google\Chrome\Application\chrome.exe","-t", "10","-f","smart","--fuzz-path", "--push-pool-max", "10","-o", "json" ,'--output-json','1.json','--log-level','info', target]
	rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = rsp.communicate()
	try:
		result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
	except:
		return
	req_list = result["req_list"]
	sub_domain = result["sub_domain_list"]
	print(data1)
	print("[crawl ok]")
	print("[scanning]")
def run(data1):
	target = data1
	num = random.randint(1,len(open(r"proxy.txt",'rU').readlines()))
	print(str(num))
	proxy = str(linecache.getline('proxy.txt', num))
	cmd = ["crawlergo.exe", "-c", "C:\Program Files\Google\Chrome\Application\chrome.exe","-t", "10","-f","smart","--fuzz-path", "--push-pool-max", "10",'--push-to-proxy',proxy, target]
	rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = rsp.communicate()
	try:
		result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
	except:
		return
	req_list = result["req_list"]
	sub_domain = result["sub_domain_list"]
	print(data1)
	print("[crawl ok]")
	print("[scanning]")




file = open("targets.txt")
n=1
for text in file.readlines():
	data1 = text.strip('\n')
	main(data1,n)
	#json解析
	hq=os.listdir(os.curdir)
	print(hq)
	for v in hq:
		if os.path.splitext(v)[1] == '.json':
			print(v)
			dk = open(v, 'r', encoding='utf-8')
			read = dk.read()
			#print(read)
			
			with open(read,'r') as load_f:
				load_dict = json.load(load_f)
				'''
				print(load_dict)
				print('\n\n')
				print(type(load_dict))
				print('\n\n')
				print(load_dict['req_list'])
				print('\n\n')
				print(type(load_dict['req_list']))
				print('\n\n')
				print(len(load_dict['req_list']))
				print(load_dict['req_list'][0])
				print('\n\n')
				print(type(load_dict['req_list'][0]))
				print('\n\n')
				'''
				print(load_dict['req_list'][0]['url'])
				#print(load_dict['req_list'][0]['method'])
				#print(load_dict['req_list'][0]['headers'])
				#print(load_dict['req_list'][0]['data'])
				#print(load_dict['req_list'][0]['source'])
			warnings.filterwarnings(action='ignore')
			os.remove(v)
			run(load_dict['req_list'][0]['url'])
	n=n+1
