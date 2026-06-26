
import pandas as pd

# 创建两个简单的 DataFrame，用国家名作为索引
oecd_bli = pd.DataFrame(
    {'幸福指数': [7.5, 6.9, 5.8, 7.2]},
    index=['挪威', '美国', '墨西哥', '丹麦']
)

gdp_per_capita = pd.DataFrame(
    {'人均GDP': [75000, 65000, 60000, 20000]},
    index=['挪威', '美国', '丹麦', '巴西']
)

print("左表 oecd_bli:")
print(oecd_bli)
print("\n右表 gdp_per_capita:")
print(gdp_per_capita)

# 通过索引进行内连接（默认 how='inner'）
full_country_stats = pd.merge(
    left=oecd_bli,
    right=gdp_per_capita,
    left_index=True,
    right_index=True
)

print("\n合并结果 full_country_stats (仅保留索引交集):")
print(full_country_stats)