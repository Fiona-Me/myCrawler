#coding:utf-8

import re
job_ability_list=[]

pattern = re.compile(r'[\u4e00-\u9fa5_a-zA-Z]+')
#pattern = re.compile(r'[\u4e00-\u9fa5]+')
#pattern = re.compile(r'[a-zA-Z]+')
f =open("d:/test.txt",encoding='UTF-8')

lines=f.readlines()
for line in lines:

	
	ability_temp =line.strip()
	ability =re.findall(pattern,line.strip())
	job_ability_list.extend(ability)
	cleaned_ability=''.join(job_ability_list)
with open("d:/tempprint.txt",'a',encoding='UTF-8') as f1:
		f1.write(cleaned_ability)
#print(cleaned_ability)
