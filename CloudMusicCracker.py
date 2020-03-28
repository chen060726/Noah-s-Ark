import requests,json
from bs4 import BeautifulSoup as bs 

def kugou(url):
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
		"Cookie": "kg_mid=68d5b18e3e7165db1fb444a4147a8de2; kg_dfid=4VuJaa1WWvCR0cWcXF4BYhqw; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1583492919,1583545197,1584595740,1585288443; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; kg_mid_temp=68d5b18e3e7165db1fb444a4147a8de2; KuGooRandom=66281585288504300; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1585288672"
	}
	print('正在解析...\n歌曲商：酷狗\n正在获取歌曲名...')
	requests.encoding="UTF-8"
	if 'hash' in url and 'album_id' in url:
		hashnum = url.find('hash')
		idnum = url.find('album_id')
	else:	
		print('错误，歌曲地址错误，无法解析出相关数据！')
		exit()
	try:
		hash = url[hashnum+5:idnum-1]
		id=url[idnum+9:]
	except:
		print('错误，歌曲地址错误，无法解析出相关数据！')
		exit()
	else:
	#print(id)
	#print(hash)
		url='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash='+hash+'&album_id='+id
		try:
			response=requests.get(url,headers=headers).text
		except:
			print('访问错误！')
			exit()
		else:
			try:
				data=json.loads(response)
				data2=data['data']
			except:
				print('解析出错！！！')
				exit()
			else:
				print('歌曲名称:'+data2['audio_name']+'\n正在获取下载地址')
				url=data2['play_backup_url']
				print('下载地址：'+url)
				try:
					response=requests.get(url)
				except:
					print('访问错误！')
					exit()
				else:
					with open(data2['audio_name']+'.mp3','wb') as audio:
						try:
							audio.write(response.content)
						except:
							print('写出文件失败！！！')
						else:
							print('下载成功！')
							audio.close()
							exit()
def kuwo(url):
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
			'Referer': 'http://www.kuwo.cn/play_detail/92272950',
		"Cookie": "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1585296121; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1585296121; _ga=GA1.2.299491069.1585296121; _gid=GA1.2.2137405587.1585296121; kw_token=18T8VYGYSTG"
	}
	print('正在解析...\n歌曲商：酷我\n正在获取歌曲名...')
	if 'play_detail' in url:
		mian=url.find('play_detail')
		miantxt=url[mian+12:]
		url1='http://www.kuwo.cn/url?format=mp3&rid='+miantxt+'&response=url&type=convert_url3&br=128kmp3&from=web&t=1585296211848&reqId=733765b1-7001-11ea-90b4-73a4a23c6a40'
	else:
		print('错误，歌曲地址错误，无法解析出相关数据！')
		exit()
	try:
		response=requests.get(url1,headers=headers).text
	except:
		print('访问错误！')
		exit()
	else:
		data = json.loads(response)
		url1=data['url']
		try:
			response=requests.get(url).text
		except:
			print('访问错误！')
			exit()
		else:
			title_num=response.find('<title data-n-head="true">')+26
			kuwo_num=response.find('_单曲在线试听_酷我音乐')
			audio_name=response[title_num:kuwo_num]
			print('歌曲名称：'+audio_name+'\n正在获取下载地址\n下载地址：'+url1)
			try:
				response=requests.get(url1)
			except:
				print('访问错误！')
				exit()
			else:
				with open(audio_name+'.mp3','wb') as audio:
					try:
						audio.write(response.content)
					except:
						print('写出文件失败！！！')
						exit()
					else:
						print('下载成功！')
						audio.close()
						exit()
def cloudm(url):
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
			'Cookie':'_ntes_nuid=e0ca90be7c3fdd828d4f6c1c3aa243da; _ntes_nnid=0b207f4f31fa2da1f36a7a9d997a8920,1585119456080; _iuqxldmzr_=32; WM_TID=TrMqXck1todBFQBQFEdpvplX36SVOcB1; WM_NI=WJEU8xifw5tuIHoybDgm%2BMSMfSCy2aI9EuBcQEXnvnXAmZ2L%2BvoKXr14viMXyJXQFtxbucZGZdTMKwLvCecPrvFW7DfSC5wUExel3fl2%2BB3aURca2%2Bs%2Bdak0RmTvFwL7dFQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6c77ebcb8c0bad16485a88ab2c55e939b8baeb54abc95afb5b54092eda0d1e42af0fea7c3b92a95968bb6bb74abbab9d6f77f8b98a19ae150a5b3e5aed247a68d8d9ab16b8be78b96c169939b988ff5669c9fa3bbb148e9aaa1acdb7af3ecba8ad054bb9698b2c580bcbebb84d94d9abc9caeca7d90aa8d86e25cb2aa8ab8b650a68d8dd6f65f87a8ab8db26eb0eee5a3b26b978ead82b121b1f5ac82ea3c92b39c97c57d90e9aca7d437e2a3; JSESSIONID-WYYY=X1QhmOOS%5CKhwS%5CC36%5CKv6spynKE8bwC6iU%2Bur7Hr%2B0yW49T4uK%5CUHEWf7gWpHSoqJFtWWNDP%5C%5CotrdGqAzuqW1QK8alADSQCgxdKzba9qNJ1T39t24H%5C4F%2B%5CSCTjyj2px84kcQH%2FPUMw2NVM2dPHttVDu2D2FBTp0aPcMA8F6oSEeuvT%3A1585355448783'
			}
	print('正在解析...\n歌曲商：网易云音乐\n正在获取歌曲名...')
	if 'id' in url:
		idnum=url.find('id')+3
		id=url[idnum:]
	else:
		print('错误，歌曲地址错误，无法解析出相关数据！')
		exit()
	try:
		response=requests.get('https://music.163.com/song?id='+id).text
	except:
		print('访问错误！')
		exit()
	else:
		try:
			title_num=response.find('<title>')+7
			title_num_1=response.find(' - 单曲 - 网易云音乐')
			audio_name=response[title_num:title_num_1]
			print('歌曲名称：'+audio_name+'\n正在获取下载地址')
		except:
			print('解析出错！！！')
			exit()
		else:
			try:
				song_url='http://music.163.com/song/media/outer/url?id='+id+'.mp3'
				print('下载地址：'+song_url+"\n正在下载")
				response=requests.get(song_url,headers=headers)
			except:
				print('访问错误！')
				exit()
		#print(response.text)
			else:

				with open(audio_name+'.mp3','wb') as audio:
					try:
						audio.write(response.content)
					except:
						print('写出文件失败！！！')
						exit()
					else:
						print('下载成功！')
						audio.close()
						exit()	
print("输入地址：",end=" ")
url=input()
#url='https://music.163.com/#/song?id=1434062381'
#url="https://www.kugou.com/song/#hash=2A3FDB4211D32CACC360E195AEB00E05&album_id=29024737"
if 'kugou' in url:
	kugou(url)
if 'kuwo' in url:
	kuwo(url)
if 'music.163' in url:
	cloudm(url)
else:
	print('无法匹配歌曲链接，本脚本只支持酷狗，酷我，网易云')
	exit()





