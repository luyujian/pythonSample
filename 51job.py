#--coding:utf-8
#python2.7.15
import requests 
from lxml import html
import pandas as pd
import time
import numpy as np
from pyecharts import Bar
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding("utf8")

def getOnePageJobData(url):
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
	respone = requests.get(url,headers=headers)
	domText = html.etree.HTML(respone.content)
	JobData = domText.xpath("//*[@id='resultList']/div[@class='el']")
	print len(JobData)
	jobsData = []
	for job in JobData:
		jobRecord = {}
		t1 = job.xpath("./p/span/a//text()")[0].strip()
		jobRecord["t1"] = t1
		t2 = job.xpath('./span[@class="t2"]/a//text()')[0]
		jobRecord["t2"] = t2
		t3 =  job.xpath('./span[@class="t3"]//text()')[0]
		jobRecord["t3"] = t3
		elt4 = job.xpath('./span[@class="t4"]//text()')
		if len(elt4)>0:
			t4 =  elt4[0]
		else:
			t4 = 0
		jobRecord["t4"] = t4
		t5 =  job.xpath('./span[@class="t5"]//text()')[0]
		jobRecord["t5"] = t5
		jobsData.append(jobRecord)
	return jobsData
#（北京地区，互联网/电子商务行业，后端开发 职位）数据画像
def getHouDuanKaiFaInfo():
	url = "https://search.51job.com/list/010000,000000,0100,32,9,99,%2520,2,{0}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
	url1 = url.format(1)
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
	respone = requests.get(url1,headers=headers)
	domText = html.etree.HTML(respone.content)
	totalPage = domText.xpath('//*[@id="hidTotalPage"]/@value')[0]
	jobsDataInfo = []
	print "Start : %s" % time.ctime()
	for i in range(1,int(totalPage)):
		requestUrl = url.format(i)
		jobsDataInfo+=getOnePageJobData(requestUrl)
		# 延迟2秒执行
		time.sleep(2)
	#,columns=[u"职位",u"公司",u"工作地点",u"薪资",u"发布时间"]
	jobsDf = pd.DataFrame(jobsDataInfo)
	# 修改列名
	jobsDf = jobsDf.rename(columns={"t1":u"职位","t2":u"公司","t3":u"工作地点","t4":u"薪资","t5":u"发布时间"})
	print jobsDf.describe()
	jobsDf.to_excel("g:\\houtaikaifajob.xlsx")
	print "Start : %s" % time.ctime()

def unique_num(x):
	return len(np.unique(x))

#公司数据、职位数据分析
def analyseJobData():
	jobsDf = pd.read_excel("g:\\houtaikaifajob.xlsx")
	df1 = jobsDf.groupby(["发布时间"]).agg({"公司":unique_num,"职位":"count"})
	columns = df1.index
	zhiweiData = df1["职位"]
	gongsiData = df1["公司"]
	bar =  Bar("2020年招聘数据分析", "后端开发招聘数据",width=1300,height=400)
	bar.add("职位数量", columns, zhiweiData, mark_line=["average"], mark_point=["max", "min"], is_datazoom_show=True)
	bar.add("公司数量", columns, gongsiData, mark_line=["average"], mark_point=["max", "min"])
	bar.render()
#开发语言招聘排行
def top15KaiFaYanData():
	jobsDf = pd.read_excel("g:\\houtaikaifajob.xlsx")
	df1 = jobsDf.groupby([u"职位"]).agg({u"公司":"count"})
	print df1.sort_values([u"公司"],ascending=False)
	columns = df1.index
#招聘公司排行
def top20GongsiData():
	jobsDf = pd.read_excel("g:\\houtaikaifajob.xlsx")
	df1 = jobsDf.groupby(["公司"]).agg({"职位":"count"})
	df1 = df1.sort_values(["职位"],ascending=False).head(20)
	print df1
	print df1.sort_values(["职位"],ascending=False).sum()
	'''df1.plot()
	plt.rcParams['font.sans-serif']=['SimHei']
	plt.show()
	'''
	columns = df1.index.tolist()
	zhiweiData = df1["职位"]
	bar =  Bar("2020年招聘数据分析", "招聘公司职位数量",width=1300,height=400)
	bar.add("职位数量", columns, zhiweiData, mark_line=["average"], mark_point=["max", "min"])
	bar.render()

def main():
	#toutiaoZhaoPin()
	#top20GongsiData()
	#top15ZhiWeiData()
	#analyseJobData()
	getHouDuanKaiFaInfo()

if __name__ == '__main__':
	main()