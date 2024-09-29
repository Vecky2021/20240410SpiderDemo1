import matplotlib.pyplot as plt

# 设置字体大小，避免中文显示问题（如果不需要中文可以跳过这步）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 创建一个新的图形和坐标轴
fig, ax = plt.subplots()

# 遍历九九乘法表的每一行和列
for i in range(1, 10):
    for j in range(1, i + 1):
        # 计算乘法结果并转换为字符串，同时格式化对齐
        text = f"{j}x{i}={i * j}"
        ax.text(j - 0.5, 9 - i, text, ha='center', va='center', fontsize=12)

    # 设置坐标轴刻度，使其不显示（因为我们会手动添加文字）
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# 设置图形标题
ax.set_title('九九乘法表', fontsize=16)

# 调整坐标轴范围，确保所有文字都在图形内
ax.set_xlim(0, 9)
ax.set_ylim(0, 10)

# 设置网格线为不可见（默认是没有的，这里只是为了说明）
ax.grid(False)

# 保存图片
plt.savefig('multiplication_table.png', dpi=300)

# 显示图片（可选，如果你是在Jupyter Notebook等环境中运行）
plt.show()