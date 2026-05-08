import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

# 获取脚本所在目录，确保图片路径正确
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "california.png")

# 读取背景图片
bg_img = mpimg.imread(img_path)

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 底层：显示图片，zorder=0
ax.imshow(bg_img, extent=[0, 10, 0, 6], aspect="auto", zorder=0)

# 上层：绘制一条简单的折线图，zorder=2
x = np.linspace(0, 10, 50)
y = 3 + 1.5 * np.sin(x)
ax.plot(x, y, color="red", linewidth=2, zorder=1, label="sin curve")

ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Multi-layer Plot: Background Image + Line Plot")
ax.legend()

#plt.savefig("two-layers-plot.png", dpi=100)
#ax.figure.savefig("two-layers-plot1.png", dpi=100)
fig.savefig("two-layers-plot2.png", dpi=100, bbox_inches="tight") # bbox_inches="tight" 可以去掉图像周围的空白边距

#plt.show()
