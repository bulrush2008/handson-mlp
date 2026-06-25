
from pathlib import Path
import urllib.request

datapath = Path() / "datasets" / "lifesat"
datapath.mkdir(parents=True, exist_ok=True) # create the directory if it doesn't exist

data_root = "https://github.com/ageron/data/raw/main/"

for filename in ("oecd_bli.csv", "gdp_per_capita.csv"):
    url = data_root + "lifesat/" + filename
    filepath = datapath / filename
    if not filepath.is_file():  # check if the file already exists
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filepath)
    else:
        print(f"{filename} already exists, skipping download.")
"""
# 这段代码也是正确的，且更加简洁
for filename in ("oecd_bli.csv", "gdp_per_capita.csv"):
    if not (datapath / filename).is_file():
        print("Downloading", filename)
        url = data_root + "lifesat/" + filename
        urllib.request.urlretrieve(url, datapath / filename)
"""