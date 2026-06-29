
import numpy as np
import pandas as pd
from pathlib import Path

#======================== 第一种方式 ===========================
def shuffle_and_split_data(data, test_ratio, rng):
    shuffled_indices = rng.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices] # 按位置索引取行，分别得到训练集和测试集的 DataFrame

housing_full = pd.read_csv(Path("./datasets/housing/housing.csv"))

# 尽管使用了种子，仍然难以保证测试集的唯一性
rng = np.random.default_rng(seed=42)
train_set, test_set = shuffle_and_split_data(housing_full, 0.2, rng)
print("第一种方式：训练集大小:", len(train_set))
print("第一种方式：测试集大小:", len(test_set))

#======================== 第二种方式 ===========================
# 对一些“固定不变的特征”进行编码，比如这里的crc32就是一种哈希编码方式。
# 这样的好处是，后面数据集若有扩充，或者删减，现在分号的训练集、测试集仍然是有效的
# 不会混乱
from zlib import crc32

def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32

def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]   # series
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]    # 按标签索引取行，分别得到训练集和测试集的 DataFrame


housing_with_id = housing_full.reset_index()  # adds an `index` column
train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "index")

# 经纬坐标是固定的，数据的删除、append、重排都不会改变它们，所以可以用它们来生成 id
housing_with_id["id"] = (housing_full["longitude"] * 1000
                         + housing_full["latitude"])
train_set, test_set = split_data_with_id_hash(housing_with_id, 0.2, "id")
print("第二种方式：训练集大小:", len(train_set))
print("第二种方式：测试集大小:", len(test_set))

#======================== 第三种方式 ===========================
# 直接适用 skl 的函数
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing_full, test_size=0.2,
                                       random_state=42)
print("第三种方式：训练集大小:", len(train_set))
print("第三种方式：测试集大小:", len(test_set))
print(test_set["total_bedrooms"].isnull().sum())
