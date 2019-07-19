import pandas as pd
import numpy as np
import re
import jieba
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.models.word2vec import Word2Vec
wkh=pd.read_excel(r'E:\OneDrive\Documents\time-manage\WorkingHours.xlsx')
wkh = wkh.iloc[:-2,]
############# 特征提取

# 合并
wkh[['标签','任务','任务详细信息','工作段细节']] = wkh[['标签','任务','任务详细信息','工作段细节']].replace(np.nan,'', regex=True)
newtab = wkh['标签'].str.cat(wkh[['任务','任务详细信息','工作段细节']],sep='    ')
newtab_list = list(map(jieba.cut,newtab))
newtab_list = [" ".join(i) for i in newtab_list]

# # doc2vec，提取特征向量
# it = [TaggedDocument(newtab_list[i].split(" "),[i]) for i in range(len(newtab_list))]
# %time model = Doc2Vec(it,dm = 0, alpha=0.1, size= 20, min_alpha=0.025)
# docvecs = model.docvecs.doctag_syn0
# model.wv.vectors.shape
# model.wv.vocab

# 基于词袋模型的计算：sklearn实现
from sklearn.feature_extraction.text import CountVectorizer
countvec = CountVectorizer(min_df=5)
resmtx = countvec.fit_transform(newtab_list) 
from sklearn.metrics.pairwise import pairwise_distances 
print(pairwise_distances(resmtx, metric = 'cosine').shape)
pairwise_distances(resmtx, metric = 'cosine')

# 使用TF-IDF矩阵进行相似度计算
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(resmtx)         # 基于词频矩阵X计算TF-IDF值
pairwise_distances(tfidf[:5],metric='cosine')

################ 开始聚类
from sklearn.cluster import KMeans
clf = KMeans(n_clusters = 5)
s = clf.fit(tfidf)
# s = clf.fit(docvecs)
print(s)

wkh['类别'] = clf.labels_
wkh.loc[wkh['类别']==1,['标签','任务','任务详细信息','工作段细节','类别']]

coln = ['date','starttime','endtime','type1','type2','type3','type4','type5','holetime']
wkh_daily = pd.DataFrame(columns=coln)

for tmp in wkh.groupby(wkh['日']):
    
    line=[tmp[0]]
    print(line)

    # 日开始
    tmp = tmp [1]
    line.append(min(tmp['开始']))
    # 日结束
    line.append(max(tmp['结束']))
    print(line)

    # 日1-5类时间、总时间
    tmplist = [0]*5
    tmp_group = tmp.groupby(tmp['类别']).sum()
    for i in tmp_group.index:
        tmplist[i] = tmp_group["持续 (小时)"][i]+tmp_group["持续 (分钟)"][i]/60

    line.extend(tmplist)
    line.append(sum(tmplist))
    print(line)

    new_df = pd.DataFrame(line).T
    new_df.columns = coln
    wkh_daily = wkh_daily.append(new_df)
    
wkh_daily.to_csv('E:/OneDrive/Documents/time-manage/wkh_daily.csv')

wc_freq = {
    'type1': {},
    'type2': {},
    'type3': {},
    'type4': {},
    'type5': {}
}
stop = ['.','；','，',',','、','的','好','要','。','A','B','与','日',
        '1','2','3','4','5','对','不',' ','（','）',
        '是','在','否','户主','','\n','-',
        '上','在','+','有','没有','进行','和','问',
        '但','时','提问','年','为','了','核实','情况','人','2018',
        '经','并','0','6','7','8','9','万','配',
        '(',')','中']

for key,value in enumerate(wc_freq):
    wc_ele1 = [newtab_list[i] for i in range(len(wkh['类别']==key)) if (wkh['类别']==key)[i]]
    wc_ele2 = pd.Series(' '.join(wc_ele1).split(" ")).value_counts()
    wc_freq[value] = wc_ele2[~wc_ele2.index.isin(stop)]

from wordcloud import WordCloud
import matplotlib.pyplot as plt

for value in wc_freq:
    wc = WordCloud(font_path='simhei.ttf',background_color='white', max_words=500)
    dict_word_pro = dict(zip(wc_freq[value].index,wc_freq[value]))
    wc.generate_from_frequencies(dict_word_pro)
    plt.imshow(wc)
    plt.axis("off")
    # plt.savefig(path+'主要问题'+yesterday+'.png', dpi=1000)
    plt.show()
