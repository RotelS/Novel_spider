#-*-coding:utf-8-*-
'''
	抓取 笔趣阁 网站
	小说《大主宰》
	写入txt

'''
import requests
import sys
import re

def onechapter(url):
	'''
	抓取一章节的文本
	'''
	strone = ''
	r = requests.get(url)
	r.encoding = 'gbk'
	#获取标题
	titlefind = re.compile(r'<title>(.*?)_大主宰_玄幻小说_笔趣阁')
	title = titlefind.findall(r.text)
	#获取文本
	pattern = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
	listshu = pattern.findall(r.text)
	#写入字符串
	strone = strone + '\n\n' + str(title[0]) + '\n\n'
	for one in listshu:
		strone = strone + '      '+str(one)+'\n'
	#返回一章节的文本内容
	print(str(title[0])+'  抓取完成\n')
	return strone

def create_txt(start,end):
	'''
	遍历网站生成TXT
	'''
	filename = '大主宰.txt'
	with open(filename,'w+') as f:
		for i in range(start,end+1):
			url = 'http://www.biquge.tv/0_1/'+str(i)+'.html'
			strone = onechapter(url)
			f.write(strone)
		f.close()

def work():
	start = input('从第几章开始：')
	end = input('到第几章结束：')
	create_txt(int(start),int(end))
	input("任务完成,按任意键结束")

if __name__ == '__main__':
	work()

