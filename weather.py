# url:
# pip install bs4 ,requests,lxml
# 安装 requests 和 beautifulsoup4
#1 step.1 抓取数据
#2 step.2 处理数据
from bs4 import BeautifulSoup
import requests
import time
import lxml
def get_temperature(url):
	headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
	'Upgrade-Insecure-Requests':'1',
	'Referer':'http://www.weather.com.cn/textFC/hb.shtml',
	'Host':'www.weather.com.cn'
	}
	req = requests.get('http://www.weather.com.cn/textFC/hb.shtml',headers=headers)
	html = req.content.decode('utf8')
	#获取省份
	#城市
	soup = BeautifulSoup(html,'lxml')
	#find_all 全体
	province = ''
	cityList =[]
	minList = []
	conMid_list = soup.find('div',class_='conMidtab')
	conMidtab2_list = conMid_list.find_all('div',class_='conMidtab2')
	for x in conMidtab2_list:
		tr_list = x.find_all('tr')[2:]
		for index,tr in enumerate(tr_list):
			#第0个tr 城市名和省份是放在一起的
			if index == 0:
				td_list = tr.find_all('td')
				province = td_list[0].text.replace('\n','')
				city = td_list[1].text.replace('\n','')
				min = td_list[7].text.replace('\n','')
				# print(province+city)
			else:
				td_list =tr.find_all('td')	
				city =td_list[0].text.replace('\n','')
				min = td_list[6].text.replace('\n','')
				cityList.append(city)
				minList.append(min)
	return cityList,minList
           
    
    		

def main():
 	urls=['http://www.weather.com.cn/textFC/hb.shtml',
 	      'http://www.weather.com.cn/textFC/db.shtml',
 	      'http://www.weather.com.cn/textFC/hd.shtml',
 	      'http://www.weather.com.cn/textFC/hn.shtml',
 	      'http://www.weather.com.cn/textFC/xb.shtml',
 	      'http://www.weather.com.cn/textFC/xn.shtml']
 	for url in urls:
 	    cityList,minList = get_temperature(url)
 	    print(cityList)
 	    print(minList)
 	    time.sleep(2)        

if __name__ == '__main__':
	main()

	
