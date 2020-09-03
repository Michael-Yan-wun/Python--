#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#導入資料並做資料前處理
import json
import random
import re
import jieba
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

#建立Jieba模型
jieba.load_userdict("stopwords.txt")

#引入資料
import pandas as pd
df = pd.read_json('Output.json')

#轉成List處理
NewsContent = df['NewsContent'].values.tolist()
NewsTitle = df['NewsTitle'].values.tolist()
ALMkeywords = df['AMLKeyword'].values.tolist()
NewsUrl = df['NewsUrl'].values.tolist()
NewsTime = df['NewsTime'].values.tolist()
CtyName = df['CtyName'].values.tolist()
LocName = df['LocName'].values.tolist()
PplName = df['PplName'].values.tolist()
ComName = df['ComName'].values.tolist()

#引入stopwords
STOP_WORDS_DIR = 'stopwords.txt'
with open(STOP_WORDS_DIR, encoding='utf8') as f:
    stopwords = f.read().splitlines()

#去除繁體中文以外的英文、數字、符號
rule = re.compile(r"[^\u4e00-\u9fa5]")
NewsContent = [list(jieba.cut(rule.sub('', content))) for content in NewsContent]

#過濾stopwords
for idx, content in enumerate(NewsContent):
    NewsContent[idx] = ' '.join([word for word in content if word not in stopwords])

