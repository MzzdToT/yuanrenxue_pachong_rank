import requests
import re

#获取5页数据求和，get参数base64加密、指定ua、cookie

session = requests.session()
headers = {
	'User-Agent': 'yuanrenxue.project',
	#传入自己的sessionid
	'cookie':'sessionid=rej5bjhw82clsmfqv4i7beb3qaqnn77w'
}

url1='http://match.yuanrenxue.com/match/13'
rsp = session.get(url1,headers=headers)
#正则匹配cookie
reg=re.compile("'([a-zA-Z0-9=|_])'")

result=reg.findall(rsp.text)
#连接元组
cookie=''.join(result)
#分割关键字
key,value=cookie.split('=')
session.cookies.set(key,value)
sum=0

for i in range(1,6):
	headers = {
	'User-Agent': 'yuanrenxue.project',}
	url = 'http://match.yuanrenxue.com/api/match/13?page=' + str(i)
	print(url)
	r = session.get(url=url,headers=headers)
	#相应内容转换为json格式
	r = r.json()
	print(r)
	#获取关键字为data的内容
	data = r.get('data')
	for d in data:
		sum= sum + d['value']
print(sum)