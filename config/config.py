# 插件的配置文件
from typing import Optional

from pydantic import Extra, BaseModel
# 用户的体力值上限，默认160
MAX_STAMINA = 160

# 体力值多长时间回复1点，默认是8分钟
STAMINA_RESTORE = 8

# 圣遗物副属性有4个级别，这里设置强化时4个级别出现的概率，默认是40% 30% 20% 10%
SECONDARY_LEVEL_PROBABILITY = [0.4, 0.3, 0.2, 0.1]

# 强化圣遗物需要的强化点数，第一个值是0级自带的点数，第二个是0级到1级消耗的点数，第3个是1级到2级消耗的点数
CONSUME_STRENGTHEN_POINTS = [
    3780,
    3000,
    3725,
    4425,
    5150,
    5900,
    6675,
    7500,
    8350,
    9225,
    10125,
    11050,
    12025,
    13025,
    15150,
    17600,
    20375,
    23500,
    27050,
    31050,
    35575,
]


class Config(BaseModel, extra=Extra.ignore):
    use_pic: Optional[bool] = False
