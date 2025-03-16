import os
import pandas as pd
from snownlp import SnowNLP
import jieba
# current_dir = os.path.dirname(os.path.abspath(__file__))
# df = pd.read_csv(f"{current_dir}\\week3.csv")

# # 处理分词后的评论（将空格连接为连续文本）

# df = df[df['comment_text'].str.strip().astype(bool)]  # 过滤空字符串和纯空格文本
# df = df.dropna(subset=['comment_text'])               # 删除NaN值
# df['comment_text'] = df['cus_comment'].str.replace(' ', '')

# # 转换评分列为数值型
# rating_map = {'非常好': 4, '很好': 3, '好': 2, '一般': 1}
# for col in ['kouwei', 'huanjing', 'fuwu']:
#     df[f'{col}_score'] = df[col].map(rating_map)

# # 定义情感分析函数
# def analyze_sentiment(text):
#     return SnowNLP(text).sentiments

# # 对每条评论进行情感分析
# df['sentiment_score'] = df['comment_text'].apply(analyze_sentiment)

# # 查看情感分数与评分的相关性
# print(df[['sentiment_score', 'stars']].corr())

# # 提取每条评论的关键词（Top5）
# def get_keywords(text):
#     s = SnowNLP(text)
#     return s.keywords(5)

# df['keywords'] = df['comment_text'].apply(get_keywords)


# # 按月份分析情感均值
# monthly_sentiment = df.groupby('month')['sentiment_score'].mean()

# # 可视化结果
# import matplotlib.pyplot as plt
# plt.figure(figsize=(10,5))
# monthly_sentiment.plot(kind='bar')
# plt.title('Monthly Sentiment Trend')
# plt.ylabel('Average Sentiment Score')
# plt.show()


# # 分析不同维度的评分关系
# dimensions = ['kouwei_score', 'huanjing_score', 'fuwu_score']
# corr_matrix = df[dimensions + ['sentiment_score']].corr()

# # 绘制热力图
# import seaborn as sns
# sns.heatmap(corr_matrix, annot=True)
# plt.title('Correlation Between Different Scores')
# plt.show()

text = '中午 吃 完 了 所谓 的 早茶 回去 放下 行李 休息 了 会 就 来 吃 下午茶 了 服务 两层楼 楼下 只能 收 现金 楼上 可以 微信 支付宝 先找 座位 再点 单 环境 人 很多 去 的 那 时候 还 下雨 楼下 楼上 座无虚席 可见 生意 真是 好 啊 芝麻糊 其实 是 芝麻糊 加 了 汤 丸 我 觉得 这个 不太腻 所以 吃 了 挺 多 双皮奶 双皮奶 第一口 的 味道 我 是 很 喜欢 但是 吃 多 了 有点 腻 碗 的 分量 不小 店里 吃 的 挺 多 不过 不饿 也 就 点 了 个 招牌 的 尝尝 再有 机会 去 的话 换 个别 的 尝尝'

s = SnowNLP(text)

print(s.sentiments)