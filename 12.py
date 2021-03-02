import requests
import base64

#获取5页数据求和，get参数base64加密、指定ua、cookie
sum=0
headers = {'User-Agent': 'yuanrenxue.project',
			#cookie使用时替换
			'Cookie':'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1614581362; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1614581683; qpfccr=true; no-alert2=true; tk=4059960744802229743; sessionid=rej5bjhw82clsmfqv4i7beb3qaqnn77w; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1614581652; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1614581652'
}
for i in range(1,6):
	str1 = 'yuanrenxue' + str(i)
	base=str(base64.b64encode(str1.encode("utf-8")),"utf-8")
	url = 'http://match.yuanrenxue.com/api/match/12?page=' + str(i) +'&m=' + base
	print(url)
	r = requests.get(url=url,headers=headers)
	#相应内容转换为json格式
	r = r.json()
	print(r)
	#获取关键字为data的内容
	data = r.get('data')
	for d in data:
		sum= sum + d['value']
print(sum)