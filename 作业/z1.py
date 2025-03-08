import jieba
import re

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns

stopterms = []
with open("作业\\cn_stopterms.txt", "r") as file:
    for line in file:
        stopterms.append(line.strip())

lines = []
with open("作业//week2.txt", "r") as  file:
    for line in file:
        line = re.sub(r'[^\u4e00-\u9fa5]', '', line)
        lines.append(' '.join(jieba.lcut(line)))

vectorizer = CountVectorizer(tokenizer=lambda x: x.split(),
                             stop_words = stopterms)
tf_matrix = vectorizer.fit_transform(lines)
tfidf_transformer = TfidfTransformer()
tfidf_matrix = tfidf_transformer.fit_transform(tf_matrix)

print("\n特征词列表:", vectorizer.get_feature_names_out())

cos_sim_matrix = cosine_similarity(tfidf_matrix)
# print("\n余弦相似度矩阵:\n", np.round(cos_sim_matrix, 2))

plt.figure(figsize=(8, 6))
sns.heatmap(
    cos_sim_matrix,
    annot=True,
    xticklabels=["句子"+str(i+1) for i in range(len(lines))],
    yticklabels=["句子"+str(i+1) for i in range(len(lines))],
    cmap="YlGnBu"
)
plt.title("文本相似性热力图")
plt.show()