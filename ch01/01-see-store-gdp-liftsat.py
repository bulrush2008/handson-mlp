
from pathlib import Path
import pandas as pd

# Path() returns the current working directory
datapath = Path() / "datasets" / "lifesat"

# create the directory if it doesn't exist
if not datapath.exists():
    datapath.mkdir(parents=True, exist_ok=True)

oecd_bli = pd.read_csv(datapath / "oecd_bli.csv")
gdp_per_capita = pd.read_csv(datapath / "gdp_per_capita.csv")

#print(datapath / "oecd_bli.csv")
#print(str(datapath)+"/"+"gdp_per_capita.csv") # 这种做法无法处理“/”和“\”的差异，不能跨系统

#============== 抽取 2020 年人均 GDP 的数据 ===================
gdp_year = 2020

gdppc_col = "GDP per capita (USD)"
lifesat_col = "Life satisfaction"

# 抽取 2020 年的数据
gdp_per_capita = gdp_per_capita[gdp_per_capita["Year"] == gdp_year]

#gdp_per_capita = gdp_per_capita.drop(columns=["Code", "Year"], axis=1)
gdp_per_capita = gdp_per_capita.drop(columns=["Code", "Year"]) # 与前一行代码等价

gdp_per_capita.columns = ["Country", gdppc_col] # 重命名列名
gdp_per_capita.set_index("Country", inplace=True) # 将“Country”列设置为索引列

#print(gdp_per_capita.head())

# ============= 抽取 2020 年生活满意度的数据 ===================
oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"] # 只保留“TOT”行
#print(oecd_bli.head())
#print(oecd_bli.columns)
oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
#print(oecd_bli[[lifesat_col]].head(10))

#===== 工作逻辑：合并两数据集后，再抽取 GDP per capita 和 Life satisfaction 两列数据 ===================
# merge 默认做内连接，及两数据的交集
# 两个表的行索引（即国家名）
# 效果：行对齐取交集，列合并，缺失的数据被自动排除
# 如果希望保留某一方的全部国家，可以设置 how='left' 或 how='right'
full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                              left_index=True, right_index=True)
#print(full_country_stats.head(20))
full_country_stats.sort_values(by=gdppc_col, inplace=True)
full_country_stats = full_country_stats[[gdppc_col, lifesat_col]]

# To illustrate the risk of overfitting, I use only part of the data in most figures
# (all countries with a GDP per capita between `min_gdp` and `max_gdp`).
# Later in the chapter I reveal the missing countries, and show that they don't follow
#  the same linear trend at all.
min_gdp = 23_500
max_gdp = 62_500

country_stats = full_country_stats[(full_country_stats[gdppc_col] >= min_gdp) &
                                   (full_country_stats[gdppc_col] <= max_gdp)]
#print(country_stats.head())

# 将处理好的GPUPC-VSLIFE-SAT数据保存到本地，供后续使用
country_stats.to_csv(datapath / "lifesat.csv")
full_country_stats.to_csv(datapath / "lifesat_full.csv")