
import pandas as pd
import matplotlib.pyplot as plt

# 错误，这时索引是默认的整数索引，后续无法根据 "Country" 列进行索引
#country_stats = pd.read_csv("datasets/lifesat/lifesat.csv")

# 正确读入方法。因为后续要根据 "Country" 列进行索引，所以在读入时就指定 index_col="Country"
country_stats = pd.read_csv("datasets/lifesat/lifesat.csv", index_col="Country")

print(country_stats.head())

gdppc_col = "GDP per capita (USD)"
lifesat_col = "Life satisfaction"

min_gdp = 23_500
max_gdp = 62_500

country_stats.plot(kind='scatter', figsize=(5, 3), grid=True,
                   x=gdppc_col, y=lifesat_col)

min_life_sat = 4
max_life_sat = 9

position_text = {
    "Turkey": (29_500, 4.2),
    "Hungary": (28_000, 6.9),
    "France": (40_000, 5),
    "New Zealand": (28_000, 8.2),
    "Australia": (50_000, 5.5),
    "United States": (59_000, 5.3),
    "Denmark": (46_000, 8.5)
}

for country, pos_text in position_text.items():
    pos_data_x = country_stats[gdppc_col].loc[country]
    pos_data_y = country_stats[lifesat_col].loc[country]
    country = "US" if country == "United States" else country
    plt.annotate(country, xy=(pos_data_x, pos_data_y),
                 xytext=pos_text, fontsize=12,
                 arrowprops=dict(facecolor='black', width=0.5,
                                 shrink=0.08, headwidth=5))
    plt.plot(pos_data_x, pos_data_y, "ro")

plt.axis([min_gdp, max_gdp, min_life_sat, max_life_sat])

plt.show()