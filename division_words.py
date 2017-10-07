#-*-coding='utf-8'-*-
import re
import jieba
jieba.load_userdict('D:/newdict.txt')
#jieba.load_userdict('D:/english_dict.txt')
import pandas as pd
import numpy
from wordcloud import WordCloud

import matplotlib.pyplot as plt 
job_ability_list=[]
f =open("d:/test.txt",encoding='UTF-8')

lines=f.readlines()
for line in lines:

	
	job_ability_list.append(line)


	cleaned_ability=''.join(job_ability_list)
#print(cleaned_ability)

segment = jieba.lcut(cleaned_ability)
words_df = pd.DataFrame({'segment':segment})
#去停用词
stopwords = pd.read_csv('D:\\stopwords.txt',index_col=False,quoting=3,sep='\t',names=['stopword'],encoding='utf-8')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
#print(words_df.head())
#词频统计
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"],ascending=False)
#print(words_stat.head())
#print(type(words_stat.head()))
#print(len(words_stat))
#print(words_stat.head(2))

length=len(words_stat)
with open('D:/division_words_num.txt','a',encoding='utf-8') as f0:
	for x in words_stat.head(length).values:
		#if x[1] != 1:
		txt = str(x[0])+','+str(x[1])
		f0.write(txt)
		f0.write('\n')
'''
word_frequence = {x[0]:x[1] for x in words_stat.head(length).values}
#print(type(word_frequence))

font=r'C:/Windodws/Fonts/simhei.ttf'
wordcloud = WordCloud(font_path=font,width=900,height=450,max_words=2000,relative_scaling=.5,background_color="black",max_font_size=80).fit_words(word_frequence)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

'''
