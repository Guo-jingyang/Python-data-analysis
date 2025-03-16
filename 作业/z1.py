import os
import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "week3.csv")

# df = pd.read_csv(file_path)
# df = df.dropna(how='any') # 清除存在空缺值的评论
# df = df.reset_index(drop=True)



# 定义情感分析函数
# def analyze_sentiment(text):
#     return SnowNLP(text).sentiments

# 对每条评论进行情感分析
# df['sentiment_score'] = df['cus_comment'].apply(analyze_sentiment)


import pickle

# with open(f"{current_dir}\\df.pkl", "wb") as file:
#     pickle.dump(df, file)

pkl_path = f'{current_dir}\\df.pkl'

with open(pkl_path, "rb") as file:
    df = pickle.load(file)


# 查看情感分数与评分的相关性
# from scipy import stats
import seaborn as sns
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# corr_matrix = df[['sentiment_score', 'stars']].corr()
# sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
# plt.title("相关系数矩阵")
# plt.show()






























# pearson_corr, pearson_p = stats.pearsonr(df['sentiment_score'], df['stars'])
# spearman_corr, spearman_p = stats.spearmanr(df['sentiment_score'], df['stars'])
# print(f"皮尔逊相关系数: {pearson_corr:.3f}, p值: {pearson_p:.4f}")
# print(f"斯皮尔曼秩相关系数: {spearman_corr:.3f}, p值: {spearman_p:.4f}")


# 散点图
plt.figure(figsize=(8, 6))
sns.regplot(
    x=df['stars'] + np.random.normal(0, 0.1, size=len(df)),  # 添加水平抖动
    y=df['sentiment_score'],
    scatter_kws={'alpha': 0.5},  # 点透明度
    line_kws={'color': 'red'}    # 回归线颜色
)
plt.title("情绪评分 vs 用户评分")
plt.xlabel("用户评分 (1-5)")
plt.ylabel("情绪评分 (0-1)")
plt.xticks([1, 2, 3, 4, 5])
plt.show()


# # 箱线图
# plt.figure(figsize=(8, 6))
# sns.boxplot(x='stars', y='sentiment_score', data=df, palette="Blues")
# plt.title("Sentiment Distribution by Rating")
# plt.xlabel("User Rating (1-5)")
# plt.ylabel("Sentiment Score (0-1)")
# plt.show()


# # 热力图
# # 计算每个评分的平均积极性
# mean_sentiment = df.groupby('stars')['sentiment_score'].mean().reset_index()

# plt.figure(figsize=(8, 6))
# sns.heatmap(
#     mean_sentiment.set_index('stars').T,
#     annot=True,
#     cmap="YlGnBu",
#     fmt=".2f",
#     cbar=False
# )
# plt.title("Average Sentiment by Rating")
# plt.xlabel("User Rating (1-5)")
# plt.ylabel("Sentiment Score (0-1)")
# plt.show()