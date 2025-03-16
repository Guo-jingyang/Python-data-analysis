import os
import pandas as pd
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "week3.csv")

df = pd.read_csv(file_path)
df['cus_comment'] = df['cus_comment'].fillna('') # 清洗数据，处理空缺值
comments = list(df["cus_comment"])

def create_analyzers(current_dir):
    '''
    此函数内部依次封装了混合情绪分析函数、唯一情绪分析函数。

    该外层函数用于惰性加载情绪字典。
    '''
    sentiments = ['joy', 'sadness', 'anger', 'disgust', 'fear']
    lexicons = {}

    # 加载情绪词典文件
    for s in sentiments:
        with open(f'{current_dir}\\{s}.txt', 'r') as f:
            lexicons[s] = set(line.strip() for line in f)

    # 混合情绪分析函数
    def mixed_analysis(text):
        counts = {s: 0 for s in sentiments}
        words = text.split()
        total = 0
        
        for word in words:
            for s in sentiments:
                if word in lexicons[s]:
                    counts[s] += 1
                    total += 1
                    break # 假设一个词只属于一个情绪类别
        
        if total == 0:
            return {s: 0.0 for s in sentiments}
        else:
            return {s: round(counts[s]/total, 2) for s in sentiments}

    # 唯一情绪分析函数
    def unique_analysis(text):
        counts = {s: 0 for s in sentiments}
        words = text.split()

        for word in words:
            for s in sentiments:
                if word in lexicons[s]:
                    counts[s] += 1
                    break

        max_count = max(counts.values())
        if max_count == 0:
            return 'neutral' # 无情绪词的情况

        if (list(counts.values()).count(max_count) > 1):
            return 'complicated' # 不同情绪的情绪词出现次数相同的情况
        
        for s in sentiments:
            if counts[s] == max_count:
                if s == 'joy': return 'positive'
                else: return 'negative'

    return mixed_analysis, unique_analysis

mixed_analyzer, unique_analyzer = create_analyzers(current_dir)

# # 函数检验
# for i in range(10):
#     print(f'第{i}条评论 混合情绪分析结果：', mixed_analyzer(comments[i]))
#     print(f'第{i}条评论 唯一情绪分析结果：', unique_analyzer(comments[i]))
#     print()


def analyze_temporal_pattern(df, shop_id, sentiment_type, 
                            time_granularity, visualize=True):
    """
    该函数能够通过参数控制返回指定店铺、指定情绪的时间模式，并可视化呈现这些模式。

    参数说明：
    shop_id: 指定店铺ID, None表示所有店铺
    sentiment_type: 'joy'/'sadness'/'anger'/'disgust'/'fear'等具体情绪类型
    time_granularity: hour/weekday/month
    visualize: 是否进行可视化, 默认为True
    """

    # 指定店铺ID
    if shop_id:
        df = df[df['shopID'] == shop_id].copy() # 强制创建副本，避免产生视图（View）或副本（Copy）的不确定性

    emotion_map = {
    'positive': ['joy'],
    'negative': ['anger', 'disgust', 'fear', 'sadness']
    }

    # 调用情绪分析函数
    mixed_analyzer, unique_analyzer = create_analyzers(current_dir)

    # 混合情绪分析
    df['sentiment_vector'] = df['cus_comment'].apply(mixed_analyzer)
    df['ratio_in_one_review'] = df['sentiment_vector'].apply(lambda x: x[sentiment_type])
    # 时间序列聚合
    mixed_grouped = df.groupby(time_granularity).agg(
        total_comments=('ratio_in_one_review', 'count'),
        sentiment_comments=('ratio_in_one_review', 'sum')
    )
    mixed_grouped['sentiment_ratio'] = mixed_grouped['sentiment_comments'] / mixed_grouped['total_comments']   




    # 唯一情绪分析
    df['sentiment_of_one_review'] = df['cus_comment'].apply(unique_analyzer)
    # 时间序列聚合
    unique_grouped = df.groupby(time_granularity).agg(
        total_comments=('sentiment_of_one_review', 'count'),
        sentiment_comments=('sentiment_of_one_review', lambda x: (x == f'{sentiment_type}').sum())
    )
    unique_grouped['sentiment_ratio'] = unique_grouped['sentiment_comments'] / unique_grouped['total_comments']


    # 可视化
    if visualize:
        # 中文显示
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        plt.figure(figsize=(8,4))
        if time_granularity == 'hour':
            # 小时模式折线图
            plt.plot(mixed_grouped.index, mixed_grouped['sentiment_ratio'], marker='o', label = 'mixed analysis')
            plt.plot(unique_grouped.index, unique_grouped['sentiment_ratio'], marker='o', label = 'unique analysis')
            plt.xticks(range(0,24))
            plt.xlabel('小时')

        elif time_granularity == 'weekday':
            # 周模式折线图
            weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
            plt.plot([weekdays[i] for i in mixed_grouped.index], mixed_grouped['sentiment_ratio'], 
                     marker='o', label = 'mixed analysis')
            plt.plot([weekdays[i] for i in unique_grouped.index], unique_grouped['sentiment_ratio'],
                     marker='o', label = 'unique analysis')
            plt.xticks(range(7))
            plt.xlabel('周')


        plt.title(f"店铺ID: {shop_id}    情绪-时间尺度: {sentiment_type} - {time_granularity}")
        plt.ylabel('情绪比例')
        plt.legend()
        plt.grid(True)
        plt.show()


# # 案例1：以 小时 作为时间尺度分析店铺518986的情绪变化情况
# analyze_temporal_pattern(df, shop_id=518986, 
#                         sentiment_type='joy',
#                         time_granularity='hour')

# # 案例2：以 周 作为时间尺度分析店铺520004的情绪变化情况
# analyze_temporal_pattern(df, shop_id=520004,
#                          sentiment_type='joy',
#                         time_granularity='weekday')


df['sentiment_of_one_review'] = df['cus_comment'].apply(unique_analyzer)

sentiment_count = df['sentiment_of_one_review'].value_counts(dropna=False)
stars_count = df['stars'].value_counts(dropna=False)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# plt.pie(sentiment_count.values, labels=sentiment_count.index, autopct="%1.1f%%")
# plt.title('情绪占比情况')
# plt.show()

# plt.pie(stars_count.values, labels=stars_count.index, autopct="%1.1f%%")
# plt.title('产品评分情况')
# plt.show()


from snownlp import SnowNLP

df['comment_text'] = df['cus_comment'].str.replace(' ', '')




