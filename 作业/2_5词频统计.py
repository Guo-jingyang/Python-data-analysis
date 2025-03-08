import jieba
from collections import Counter
import re

with open("作业\\week2.txt", "r") as file:
    text = file.read()

# 文本预处理（去除非中文字符和标点）
text = re.sub(r'[^\u4e00-\u9fa5]', '', text)

# 分词
jieba.add_word('扶他林')
terms = jieba.lcut(text)

# 统计词频
# terms_counter = Counter(terms)

# terms_top10 = terms_counter.most_common(10)
# for term, count in terms_top10:
#     print(term, count)

stopterms = []
with open("作业\\cn_stopterms.txt", "r") as file:
    for line in file:
        stopterms.append(line.strip())

filtered_terms = [i for i in terms if i not in stopterms]
# filtered_counter = Counter(filtered_terms)
# filtered_top10 = filtered_counter.most_common(10)
# for term, count in filtered_top10:
#     print(term, count)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# # 删除低频词
# frequency = 500
# for term in list(filtered_counter.keys()):
#     if filtered_counter[term] < frequency:
#         del filtered_counter[term]
        
# # 词云
# wd = WordCloud(font_path="C:\\Windows\\Fonts\\simhei.ttf",
#               background_color="white")
# wd.generate_from_frequencies(filtered_counter)

# plt.imshow(wd)
# plt.axis("off")
# plt.show()

# import jieba.posseg as pseg

# words = pseg.lcut(text)

# 停用词过滤
# filtered_words = [pair for pair in words if pair.word not in stopterms]

# 词性出现频率统计
# flag_counter = Counter()
# for pair in filtered_words:
#     flag_counter[pair.flag] += 1
# for flag, count in flag_counter.most_common():
#     print(flag, count)

# 对名词和动词进行可视化
# n_counter = Counter()
# v_counter = Counter()
# for pair in filtered_words:
#     if pair.flag == 'n':
#         n_counter[pair.word] += 1
#     elif pair.flag == 'v':
#         v_counter[pair.word] += 1

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# wd1 = WordCloud(font_path="C:\\Windows\\Fonts\\simhei.ttf",
#                 background_color="white")
# wd1.generate_from_frequencies(n_counter)
# plt.imshow(wd1)
# plt.title("名词词云")
# plt.axis("off")
# plt.show()

# wd2 = WordCloud(font_path="C:\\Windows\\Fonts\\simhei.ttf",
#                 background_color="white")
# wd2.generate_from_frequencies(v_counter)
# plt.imshow(wd2)
# plt.title("动词词云")
# plt.axis("off")
# plt.show()

# 统计所有的bigram的频率
bigrams = [(filtered_terms[i], filtered_terms[i+1])
           for i in range(len(filtered_terms)-1)]
bigrams_counter = Counter(bigrams)

# 可视化高频的bigram
bigrams_top20 = bigrams_counter.most_common(20)
labels = [f"({bigram},{count})"
         for bigram, count in bigrams_top20]
counts = [count for _, count in bigrams_top20]

plt.figure(figsize=(6, 4))
plt.barh(labels[::-1], counts[::-1])
plt.xlabel('Frequency')
plt.title('Top 20 Bigrams (Filtered Stopterms)')
plt.tight_layout()
plt.show()