# 导入必要的库
import matplotlib.pyplot as plt
import ast
from collections import Counter

# 打开并读取 count.log 文件
with open("count.log", "r") as file:
    data_string = file.read()

# 转换字符串到字典
data_dict = ast.literal_eval(data_string)

# 保留数量最多的前15个键值
top_15 = dict(Counter(data_dict).most_common(20))

# 提取键和值生成列表
keys = list(top_15.keys())
values = list(top_15.values())

# 创建柱状图
plt.figure(figsize=(10, 8))  # 设置图表大小

# 绘制柱状图
plt.bar(keys, values, color='skyblue')

# 添加标题和标签
plt.title('Key Distribution')
plt.xlabel('Keys')
plt.ylabel('Frequency')

# 显示网格线
plt.grid(True)

# 自动调整x轴标签的显示
plt.xticks(rotation=45)

# 保存图表为png
plt.savefig('result.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()
