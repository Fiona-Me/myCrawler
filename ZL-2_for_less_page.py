
import requests
from bs4 import BeautifulSoup as bs
import re


def getHTMLText(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    try:
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def job_url_name_list(soup):
	to_job_url = soup.find_all('td',class_ ='zwmc')
	job_url_list=[]
	job_name_list=[]
	for job in to_job_url:
		job_name_list.append(job.find_all('a')[0].text)
		job_url_list.append(job.find_all('a')[0].attrs['href'])
	return job_url_list,job_name_list
def job_salary(soup):
	jobInfo_salary=soup.find_all('ul',class_ ='terminal-ul clearfix')
	jobsalary_temp=jobInfo_salary[0].find_all('li')[0].text
	temp=jobsalary_temp.strip().split("：")
	job_salary=temp[-1]
	return(job_salary)
def job_exp(soup):
	jobInfo_exp=soup.find_all('ul',class_ ='terminal-ul clearfix')
	jobexp_temp=jobInfo_exp[0].find_all('li')[4].text
	temp=jobexp_temp.strip().split("：")
	job_exp=temp[-1]
	return(job_exp)
def job_edu(soup):
	jobInfo_edu=soup.find_all('ul',class_ ='terminal-ul clearfix')
	jobedu_temp=jobInfo_edu[0].find_all('li')[5].text
	temp=jobedu_temp.strip().split("：")
	job_edu=temp[-1]
	return(job_edu)
def job_man(soup):
	jobInfo_man=soup.find_all('ul',class_ ='terminal-ul clearfix')
	jobman_temp=jobInfo_man[0].find_all('li')[6].text
	temp=jobman_temp.strip().split("：")
	job_man=temp[-1]
	return(job_man)
def job_ability(soup):
	job_ability_list=[]
	jobInfo_ability=soup.find_all('div',class_="tab-inner-cont")
	jobability_temp =jobInfo_ability[0].find_all('p')
	#print(jobability_temp)
	pattern = re.compile(r'[\u4e00-\u9fa5_a-zA-Z]+')
	for ability in jobability_temp:
		temp=ability.text.strip()
		#print(temp)
		ability_temp =re.findall(pattern,temp)
		job_ability_list.extend(ability_temp)
		#print(ability_temp)
	#print(job_ability_list)
	cleaned_ability=''.join(job_ability_list)
	return(cleaned_ability)

def print_hang(print_list,fpath):
	with open(fpath,'a',encoding = 'utf-8') as f:
		for txt in print_list:
			f.write(txt)
			f.write('\n')
def printList(print_list,fpath):
	with open(fpath,'a',encoding = 'utf-8') as f:
		for txt in print_list:
			f.write(txt)
def main():
	job_list=[]
	job_dict_list=[]
	
	id_name=[]
	job_id=0
	sum=0
	
	id_ability=[]
	url='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=+%E5%8C%97%E4%BA%AC&kw=%E6%95%99%E5%AD%A6%E8%AE%BE%E8%AE%A1&isadv=0&isfilter=1&p=1&bj=160200'
	count=0
	
	html_data=getHTMLText(url)#print(html_data)
	soup = bs(html_data,'html.parser')
	job={}
	job_url_list,job_name_list=job_url_name_list(soup)
	#name_all.extend(job_name_list)
	for j in range(0,len(job_url_list)):
	#for j in range(0,47):
		job_temp=[]
		id_ability_temp=[]
		id_name_temp=[]
		print('len_job_url_list',len(job_url_list))
		count+=1
		job_id+=1
		job['id']=job_id
		print('job_id:',job['id'])
				
			
		job['url']=job_url_list[j]
		job['name']=job_name_list[j]
		print('job_name:',job['name'])
	#print name_all_id.txt
		id_name_temp.append(str(job['id'])+','+job['name']+','+job['url'])
		id_name.extend(id_name_temp)

		html_data=getHTMLText(job_url_list[j])
		soup=bs(html_data,'html.parser')
		salary=job_salary(soup)
		ability=job_ability(soup)
		man=job_man(soup)
		edu=job_edu(soup)
		exp=job_exp(soup)

		#for print  ability_all.txt
		#ability_all.append(ability)

		job['salary']=salary
		job['ability']=ability
		job['man']=man
		job['edu']=edu
		job['exp']=exp
		job_dict_list.append(job)

		job_temp.append(str(job['id'])+','+job['name']+','+job['salary']+','+job['man']+','+job['edu']+','+job['exp']+','+job['ability']+','+job['url'])
		#print(job_temp[:1])
		#job_temp.append(str(job['id'])+','+job['name']+','+job['salary']+','+job['man']+','+job['ability']+','+job['url'])
		job_list.extend(job_temp)

		#id_ability_temp.append(str(job['id'])+','+job['ability']+','+job['url'])
		#id_ability.extend(id_ability_temp)




	id_name_path='D:/id_BJY.txt'
	print_hang(id_name,id_name_path)

	id_salary_man_path='D:/all_BJY.txt'
	print_hang(job_list,id_salary_man_path)
main()
