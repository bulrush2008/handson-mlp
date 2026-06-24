"""
seaborn 是一个基于 matplotlib 的 Python 数据可视化库，
- 提供了更高级的接口来创建美观且信息丰富的统计图表。
- 它使得数据可视化变得更加简单和直观，特别适合用于探索性数据分析和统计建模。

%%% 对比 matplotlib vs seaborn %%%

Matplotlib — 通用绘图工具箱
- 偏向像素级控制
- 适合创建自定义图表
- 学习曲线陡峭

Seaborn — 统计可视化专家
- 面向统计探索性分析
- DataFrame 原生支持
- 5分钟出专业统计图
"""


# 写一个简洁的代码，学习使用 seaborn 来进行数据可视化。我们将使用 seaborn 来创建一个简单的散点图，展示两个变量之间的关系。
import seaborn as sns
import matplotlib.pyplot as plt

# 加载示例数据集
tips = sns.load_dataset("tips") # 这是一个包含餐厅小费数据的示例数据集

# 1. 查看数据类型
print("数据类型:", type(tips))  # df

# 2. 查看前几行
print("\n前5行数据:")
print(tips.head())
# 3. 数据结构信息
print("\n数据信息:")
print(tips.info())
# 4. 基本统计
print("\n统计描述:")
print(tips.describe())

# 创建一个散点图，展示小费金额与账单总额之间的关系
sns.scatterplot(data=tips, x="total_bill", y="tip")
# 显示图表
plt.title("Total Bill vs Tip")
plt.savefig("c2-20260609-simple-check-seaborn.png") # 保存图表为 PNG 文件
plt.show()