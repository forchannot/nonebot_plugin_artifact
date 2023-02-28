import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from io import BytesIO

FILE_PATH = os.path.dirname(__file__)
FONT_PATH = os.path.join(FILE_PATH, "../resources/fonts/MSYH.TTC")


def draw_obtain(data_t):
    # 创建 DataFrame 对象
    df = pd.DataFrame(data_t, columns=["副本名称", "可刷取的圣遗物"])
    table_height = len(df.columns) * 1.6  # 每列宽度为 1.6 英寸
    table_width = len(df) * 0.45  # 每行高度为 0.45 英寸
    plt.rcParams["figure.figsize"] = (table_width, table_height)
    # 创建图形并绘制表格
    font_prop = fm.FontProperties(fname=FONT_PATH)
    fig, ax = plt.subplots()
    ax.axis("off")
    table = ax.table(
        cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center"
    )
    # 设置表格字体
    for cell in table.get_celld().values():
        cell.set_text_props(fontproperties=font_prop)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0)
    # 将图片保存到内存中
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=1000)
    buf.seek(0)
    # 使用 Image 对象打开保存在内存中的图片
    image_bytes = buf.getvalue()
    # 关闭 buffer 和图形
    buf.close()
    return image_bytes
