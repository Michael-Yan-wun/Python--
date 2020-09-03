#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#將內文轉換為向量值計算(Tf-idf)
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(NewsContent)
tfidf = tfidf.toarray()

##k值需用excel平均後計算得出
k = 150
Kmeans_cluster = KMeans()
content_cluster_result = Kmeans_cluster.kmeans_plus_plus(tfidf, k)
cluster = [[] for _ in range(k)]
cato = [[] for _ in range(k)]
url = [[] for _ in range(k)]
time = [[] for _ in range(k)]
Cty = [[] for _ in range(k)]
Loc = [[] for _ in range(k)]
Ppl = [[] for _ in range(k)]
Com = [[] for _ in range(k)]
Index = [[] for _ in range(k)]
for idx, c in enumerate(content_cluster_result):
    cluster[int(c)].append(NewsTitle[idx])
    cato[int(c)].append(ALMkeywords[idx])
    url[int(c)].append(NewsUrl[idx])
    time[int(c)].append(NewsTime[idx])
    Cty[int(c)].append(CtyName[idx])
    Loc[int(c)].append(LocName[idx])
    Ppl[int(c)].append(PplName[idx])
    Com[int(c)].append(ComName[idx])
    
#將訓練結果依照格式寫入list中
result_all=[]
for i in range(len(cato)):
        result_all.append({
              'cluster '+str(i):' '.join(cluster[i]),
              'keywords '+str(i):' '.join(cato[i]),
              'url '+str(i):' '.join(url[i]),
              'NewsTime '+str(i):' '.join(time[i]),
              'CtyName '+str(i):' '.join(Cty[i]),
              'LocName '+str(i):' '.join(Loc[i]),
              'PplName '+str(i):' '.join(Ppl[i]),
              'ComName '+str(i):' '.join(Com[i]),
             })
result_all

#將結果寫入json檔案
with open('Result.json','w', encoding = 'utf8' ) as f:
    json.dump(result_all,f,indent=4,ensure_ascii=False)
print("載入入檔案完成...")

